"""Acquire user-supplied references. Credentials are read only from the environment."""
import concurrent.futures, datetime, json, os, re, urllib.request, urllib.parse, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research/references'
SOURCE = Path('/workspace/attachments/6fa212e9-96c0-4dcf-999e-b6645cee15a8/Pasted text.txt')

def acquire(url):
    ident = url.split('/video/')[-1] if 'tiktok' in url else urllib.parse.parse_qs(urllib.parse.urlparse(url).query)['v'][0]
    folder = OUT / ident
    folder.mkdir(parents=True, exist_ok=True)
    record = {'url': url, 'id': ident, 'retrieved_at': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    endpoint = '/v2/tiktok/video' if 'tiktok' in url else '/v1/youtube/video'
    try:
        meta = folder / 'metadata.json'
        if meta.exists(): data = json.loads(meta.read_text())
        else:
            req = urllib.request.Request('https://api.scrapecreators.com' + endpoint + '?' + urllib.parse.urlencode({'url': url}), headers={'x-api-key': os.environ['SCRAPECREATORS_API_KEY']})
            with urllib.request.urlopen(req, timeout=45) as r: data = json.load(r)
            meta.write_text(json.dumps(data, indent=2))
        detail = data.get('aweme_detail', data)
        record.update(title=detail.get('desc', detail.get('title', '')), statistics=detail.get('statistics', {}), duration_ms=detail.get('video', {}).get('duration'), metadata='metadata.json')
        if 'tiktok' in url:
            video = folder / 'reference.mp4'
            errors = []
            for media in detail.get('video', {}).get('play_addr', {}).get('url_list', [])[:2]:
                if video.exists(): break
                try:
                    with urllib.request.urlopen(urllib.request.Request(media, headers={'User-Agent':'Mozilla/5.0'}), timeout=45) as r: payload = r.read()
                    if len(payload) < 10000: raise ValueError('Empty media response')
                    video.write_bytes(payload)
                except Exception as e: errors.append(type(e).__name__)
            record['footage_status'] = 'downloaded' if video.exists() else 'unavailable'
            record['acquisition_errors'] = errors
        else: record['footage_status'] = 'metadata_only'
    except Exception as e:
        record.update(footage_status='failed', error=type(e).__name__, http_status=getattr(e,'code',None))
    (folder / 'acquisition.json').write_text(json.dumps(record, indent=2))
    print(ident, record['footage_status'], flush=True)
    return record

if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    urls = list(dict.fromkeys(re.findall(r'https://(?:www\.tiktok\.com/@[^\s)]+/video/\d+|www\.youtube\.com/watch\?v=[\w-]+)', SOURCE.read_text())))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: records = list(pool.map(acquire, urls))
    (OUT / 'manifest.json').write_text(json.dumps(records, indent=2))
