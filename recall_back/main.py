from fastapi import FastAPI
import firebase_admin
from firebase_admin.credentials import Certificate
from app.api import api
import uvicorn


app = FastAPI()
cert: Certificate = Certificate("recall_back/secrets/firebase_service_account_key.json")
firebase_admin.initialize_app(cert)

app.include_router(api.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) # type: ignore