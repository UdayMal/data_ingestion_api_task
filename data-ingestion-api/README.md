# Data Ingestion API

## Features
- Submit ID ingestion with priorities 
- Background batch processing
- Respects 5s rate limit per batch
- Check ingestion status

## Run Locally

```bash
pytest test_app.py  : for running the app 
pip install -r requirements.txt : to install the required dependencies
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
You can check the status of ingestion API requests and Status API requests using tool like Postman
```

## Sample Output
![image](https://github.com/user-attachments/assets/a763db74-69b5-48dd-a6eb-676e766437b7)
