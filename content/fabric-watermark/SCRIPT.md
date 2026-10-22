# Your pipeline passed. Did it miss a row?

Format: 9:16 silent technical explainer, 40 seconds. No audio or presenter.
Audience: Power BI practitioners and small data teams evaluating Fabric ingestion patterns.
Editorial basis: uploaded Fabric_Content_Gap_Analysis.html, W03 incremental correctness pilot.

## Script for a later voice pass
Your pipeline passed. But did every row arrive?
Here is a tiny synthetic example. Two rows share a timestamp. The loader reads one row, then saves that timestamp as its checkpoint.
The next page asks for timestamps greater than the checkpoint. The other row at the same time disappears from the result.
For this fixed snapshot, add a stable ID to the cursor and sort by both fields.
Now all three keys arrive. Upsert the same batch twice: still three destination rows.
That fixes this timestamp tie. Late arrivals, updates, deletes and recovery still need their own tests.
Test the output, not just the green checkmark.

The video uses shorter on-screen phrases in scenes.json. Its timing is for silent reading, not measured narration.

## Evidence
| Claim | Evidence | Boundary |
|---|---|---|
| A timestamp-only per-page checkpoint can skip tied rows | src/lab.py, naive_ids [101,103], missing 102 | Deliberately unsafe example with page size 1; not a claim about every Fabric connector |
| A composite cursor retrieves all rows in this snapshot | src/lab.py, fixed_ids [101,102,103] | Requires a stable, ordered snapshot and unique tie-breaker |
| Repeated key-based upserts leave 3 destination rows | src/lab.py, target_count_after_two_upserts = 3 | Demonstrates destination idempotency for this batch, not crash consistency |
| W03 is an editorial pilot worth testing | User-provided audit, Six pilots / W03 | User research, not independently validated demand |

No Fabric workspace, connector, capacity, or cloud pipeline was exercised. The screen visuals are original representations of measured local SQLite results, not Fabric UI screenshots.
