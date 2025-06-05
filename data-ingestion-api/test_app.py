# import pytest
# from httpx import AsyncClient
# from main import app
# import asyncio

# @pytest.mark.asyncio
# async def test_priority_and_rate_limit():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         res1 = await ac.post("/ingest", json={"ids": [1,2,3,4,5], "priority": "MEDIUM"})
#         res2 = await ac.post("/ingest", json={"ids": [6,7,8,9], "priority": "HIGH"})
#         ingestion1 = res1.json()["ingestion_id"]
#         ingestion2 = res2.json()["ingestion_id"]
#         await asyncio.sleep(16)
#         status1 = await ac.get(f"/status/{ingestion1}")
#         status2 = await ac.get(f"/status/{ingestion2}")
#         assert status2.json()["batches"][0]["ids"] == [6,7,8]
#         assert status2.json()["batches"][0]["status"] == "completed"
#         assert status1.json()["status"] == "completed"

import pytest
import asyncio
from httpx import AsyncClient
from main import app
from worker import process_batches

@pytest.mark.asyncio
async def test_priority_and_rate_limit():
    # Start the background worker manually
    #asyncio.create_task(process_batches())
    task = asyncio.create_task(process_batches())
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res1 = await ac.post("/ingest", json={"ids": [1, 2, 3, 4, 5], "priority": "MEDIUM"})
        res2 = await ac.post("/ingest", json={"ids": [6, 7, 8, 9], "priority": "HIGH"})

        ingestion1 = res1.json()["ingestion_id"]
        ingestion2 = res2.json()["ingestion_id"]

        # Wait enough time for all batches to be processed
        await asyncio.sleep(21)

        status1 = await ac.get(f"/status/{ingestion1}")
        status2 = await ac.get(f"/status/{ingestion2}")

        print("STATUS 1:", status1.json())
        print("STATUS 2:", status2.json())

        assert status2.json()["batches"][0]["ids"] == [6, 7, 8]
        assert status2.json()["batches"][0]["status"] == "completed"
        assert status1.json()["status"] == "completed"
        task.cancel()
