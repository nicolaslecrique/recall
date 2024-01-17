from datetime import datetime
from dataclasses import dataclass
from typing import List
from uuid import UUID


@dataclass
class User:
    firebase_auth_uid: str
    id: UUID
    email: str


@dataclass
class Workspace:
    id: UUID


@dataclass
class Item:
    id: UUID
    title: str
    text_content: str
    last_modification_date: datetime


@dataclass
class WorkspaceData:
    workspace: Workspace
    items: List[Item]


@dataclass
class UserData:
    user: User
    workspaces_data: List[WorkspaceData]
