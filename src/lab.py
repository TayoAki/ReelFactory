"""Synthetic checkpoint counterexample; no Fabric service is invoked."""
import json, sqlite3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def run():
    db = sqlite3.connect(':memory:')
    db.executescript('CREATE TABLE source(id INTEGER PRIMARY KEY, modified TEXT); CREATE TABLE target(id INTEGER PRIMARY KEY, modified TEXT);')
    db.executemany('INSERT INTO source VALUES (?, ?)', [(101,'10:00:00'),(102,'10:00:00'),(103,'10:01:00')])
    # A deliberately unsafe page checkpoint: save timestamp after each page.
    first = db.execute('SELECT * FROM source ORDER BY modified,id LIMIT 1').fetchall()
    rest = db.execute('SELECT * FROM source WHERE modified > ? ORDER BY modified,id', (first[-1][1],)).fetchall()
    naive = first + rest
    # A stable composite cursor handles equal timestamps in a static snapshot.
    cursor = ('',0); fixed=[]
    while True:
        page=db.execute('SELECT * FROM source WHERE (modified,id) > (?,?) ORDER BY modified,id LIMIT 1',cursor).fetchall()
        if not page: break
        fixed += page; cursor=(page[-1][1],page[-1][0])
    for _ in range(2):
        db.executemany('INSERT INTO target VALUES (?,?) ON CONFLICT(id) DO UPDATE SET modified=excluded.modified',fixed)
    target=db.execute('SELECT * FROM target ORDER BY id').fetchall()
    assert [r[0] for r in naive]==[101,103]
    assert [r[0] for r in fixed]==[101,102,103]
    assert target==fixed
    result={'scope':'Local SQLite synthetic snapshot; not a Microsoft Fabric execution', 'source':[{'id':i,'modified':t} for i,t in fixed], 'naive_ids':[r[0] for r in naive], 'missed_ids':[102], 'fixed_ids':[r[0] for r in fixed], 'target_count_after_two_upserts':len(target), 'checks':{'counterexample_reproduced':True,'composite_cursor_complete':True,'repeat_upsert_no_duplicates':True}, 'limitations':['Composite cursor only demonstrates stable pagination over this fixed snapshot.','Late arrivals, updates behind the cursor, deletes, null timestamps and concurrent writes need separate source-specific strategies.','Checkpoint persistence must be coordinated with destination writes.']}
    out=ROOT/'content/fabric-watermark/evidence.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    return result
if __name__=='__main__':run()
