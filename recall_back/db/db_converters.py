from typing import List

from db.db_model import DbUser, DbItem, DbWorkspace
from model.model import User, Item, Workspace


def to_user(db_user: DbUser) -> User:
    return User(id=db_user.id, firebase_auth_uid=db_user.firebase_auth_uid, email=db_user.email)


def to_item(db_item: DbItem) -> Item:
    return Item(
        id=db_item.id,
        title=db_item.title,
        text_content=db_item.text_content,
        last_modification_date=db_item.last_modification_date,
    )


def to_workspace(db_workspace: DbWorkspace) -> Workspace:
    return Workspace(id=db_workspace.id)
