from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from app.api import api
import uvicorn


app = FastAPI()
#cred = credentials.Certificate("secrets/firebase_service_account_key.json")
#firebase_admin.initialize_app(cred)

app.include_router(api.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) # type: ignore