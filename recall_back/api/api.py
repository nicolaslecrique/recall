from typing import Dict

from fastapi import APIRouter, Header
from firebase_admin import auth

from api.api_converters import to_api_user_data_snapshot
from api.api_model import ApiUserDataSnapshot
from model.crud_service import CrudService
from model.model import UserData

router = APIRouter()
crud_service: CrudService = CrudService()

@router.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


@router.get("/user")
async def get_or_create(authorization: str = Header()) -> ApiUserDataSnapshot:
    id_token: str = authorization[7:]  # remove "Bearer " prefix
    decoded_token: Dict[str, str] = auth.verify_id_token(id_token)
    uid: str = decoded_token["uid"]
    email: str = decoded_token["email"]
    user_data: UserData = crud_service.get_or_create_user(uid, email)
    snapshot: ApiUserDataSnapshot = to_api_user_data_snapshot(user_data)
    return snapshot


@router.put("/item")
async def create_or_update_item(authorization: str = Header()):
    pass
