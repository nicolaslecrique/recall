from datetime import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class User:
    firebase_auth_uid: str
    uri: str
    email: str


@dataclass
class Workspace:
    uri: str


@dataclass
class Item:
    uri: str
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
