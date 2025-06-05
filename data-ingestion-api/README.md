# Data Ingestion API

## Features
- Submit ID ingestion with priorities 
- Background batch processing
- Respects 5s rate limit per batch
- Check ingestion status

## Run Locally

```bash
pytest test_app.py 
pip install -r requirements.txt : to install the required dependencies
uvicorn main:app --host 0.0.0.0 --port 5000 --reload : to run the server of FastAPI App
You can check the status of ingestion(/ingest) API requests and Status API (/status/<ingestion_id>) requests using tools like Postman or FastAPI Swagger UI
```

## Sample Output
![image](https://github.com/user-attachments/assets/a763db74-69b5-48dd-a6eb-676e766437b7)
