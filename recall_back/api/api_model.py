from datetime import datetime
from typing import List
from pydantic import BaseModel


class ApiUserInfo(BaseModel):
    uri: str


class ApiItemSnippet(BaseModel):
    uri: str
    title: str
    text_content: str
    last_modification_date: datetime


class ApiItemFullData(BaseModel):
    snippet: ApiItemSnippet


class ApiUserDataSnapshot(BaseModel):
    userInfo: ApiUserInfo
    items: List[ApiItemSnippet]
