from dataclasses import dataclass

from fastapi import APIRouter, Depends, Header
from firebase_admin import auth # type: ignore

from api.api_converters import to_api_user_data_snapshot
from api.api_model import ApiUserDataSnapshot
from model.crud_service import CrudService
from model.model import UserData

router: APIRouter = APIRouter()
crud_service: CrudService = CrudService()

@router.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}

@dataclass
class UserIdentity:
    uid: str
    email: str


async def get_identity(authorization: str = Header()) -> UserIdentity:
    id_token: str = authorization[7:]  # remove "Bearer " prefix
    decoded_token: dict[str, str] = auth.verify_id_token(id_token) # type: ignore
    return UserIdentity(decoded_token["uid"], decoded_token["email"]) # type: ignore


@router.get("/user")
async def get_or_create(identity: UserIdentity = Depends(get_identity)) -> ApiUserDataSnapshot:
    user_data: UserData = crud_service.get_or_create_user(identity.uid, identity.email)
    snapshot: ApiUserDataSnapshot = to_api_user_data_snapshot(user_data)
    return snapshot


@router.put("/item")
async def create_or_update_item(identity: UserIdentity = Depends(get_identity)):
    pass
