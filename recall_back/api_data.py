from pydantic import BaseModel


class ApiUser(BaseModel):
    uri: str


