from collections import defaultdict
from uuid import uuid4
import heapq
from typing import Dict, List
import time

# Format: ingestion_id → {batches: [...], status: ...}
ingestions: Dict[str, dict] = {}

# Priority Queue [(priority_order, created_time, ingestion_id, batch_index)]
# Lower number = higher priority
queue = []
priority_order_map = {"HIGH": 1, "MEDIUM": 2, "LOW": 3}

def create_batches(ids, priority):
    batches = [ids[i:i+3] for i in range(0, len(ids), 3)]
    ingestion_id = str(uuid4())
    ingestions[ingestion_id] = {
        "status": "yet_to_start",
        "batches": []
    }
    now = time.time()
    for i, batch in enumerate(batches):
        batch_id = str(uuid4())
        batch_data = {
            "batch_id": batch_id,
            "ids": batch,
            "status": "yet_to_start"
        }
        ingestions[ingestion_id]["batches"].append(batch_data)
        heapq.heappush(queue, (priority_order_map[priority], now, ingestion_id, i))
    return ingestion_id

def get_status(ingestion_id):
    ingestion = ingestions.get(ingestion_id)
    if not ingestion:
        return None

    statuses = [batch["status"] for batch in ingestion["batches"]]
    if all(s == "yet_to_start" for s in statuses):
        ingestion["status"] = "yet_to_start"
    elif all(s == "completed" for s in statuses):
        ingestion["status"] = "completed"
    else:
        ingestion["status"] = "triggered"
    return ingestion
