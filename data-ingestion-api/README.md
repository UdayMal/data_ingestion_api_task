# Data Ingestion API

## Features
- Submit ID ingestion with priorities 
- Background batch processing
- Respects 5s rate limit per batch
- Check ingestion status

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
