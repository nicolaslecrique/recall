from datetime import datetime
from typing import List
from uuid import UUID
from pydantic import BaseModel


class ApiUserInfo(BaseModel):
    id: UUID

class ApiItem(BaseModel):
    id: UUID
    title: str
    text_content: str
    last_modification_date: datetime

class ApiUserDataSnapshot(BaseModel):
    userInfo: ApiUserInfo
    items: List[ApiItem]
