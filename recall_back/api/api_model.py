from datetime import datetime
from typing import List
from pydantic import BaseModel


class ApiUserInfo(BaseModel):
    uri: str

class ApiItemData(BaseModel):
    title: str
    text_content: str

class ApiItem(BaseModel):
    uri: str
    data: ApiItemData
    last_modification_date: datetime

class ApiUserDataSnapshot(BaseModel):
    userInfo: ApiUserInfo
    items: List[ApiItem]
