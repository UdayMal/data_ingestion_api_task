from fastapi import FastAPI, BackgroundTasks
from models import IngestRequest
from storage import create_batches, get_status
from worker import process_batches
import asyncio

app = FastAPI()
@app.on_event("startup")
async def startup():
    asyncio.create_task(process_batches())

@app.post("/ingest")
async def ingest(request: IngestRequest):
    ingestion_id = create_batches(request.ids, request.priority)
    return {"ingestion_id": ingestion_id}

@app.get("/status/{ingestion_id}")
async def status(ingestion_id: str):
    result = get_status(ingestion_id)
    if not result:
        return {"error": "Invalid ingestion_id"}
    return {"ingestion_id": ingestion_id, **result}
