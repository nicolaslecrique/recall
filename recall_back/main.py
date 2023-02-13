from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from api import api


app = FastAPI()
cred = credentials.Certificate("secrets/firebase_service_account_key.json")
firebase_admin.initialize_app(cred)

app.include_router(api.router)

