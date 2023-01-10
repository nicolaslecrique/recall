from fastapi import FastAPI, Header
from api_data import ApiUser
import firebase_admin
from firebase_admin import credentials, auth

app = FastAPI()
cred = credentials.Certificate("secrets/firebase_service_account_key.json")
firebase_admin.initialize_app(cred)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user")
async def get_or_create(authorization: str = Header()):
    id_token = authorization[7:]  # remove "Bearer " prefix
    decoded_token = auth.verify_id_token(id_token)
    uid = decoded_token['uid']

    return ApiUser(uri="test")


@app.put("/item")
async def create_or_update_item(authorization: str = Header()):
    pass


# get user items
@app.get("/items")
async def get_items(authorization: str = Header()):
    pass
