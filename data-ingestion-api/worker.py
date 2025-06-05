import asyncio
import time
from storage import queue, ingestions

async def process_batches():
    while True:
        if queue:
            priority, created_time, ingestion_id, batch_idx = queue.pop(0)
            batch = ingestions[ingestion_id]["batches"][batch_idx]
            batch["status"] = "triggered"
            await asyncio.sleep(1)  # Simulate external API call
            await asyncio.sleep(4)  # Respect 5s rate-limit
            batch["status"] = "completed"
        else:
            await asyncio.sleep(1)
