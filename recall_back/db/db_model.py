from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, MetaData
from sqlalchemy.orm import declarative_base

DbBase = declarative_base(metadata=MetaData(schema="recall_db_schema"))


class DbWorkspace(DbBase):
    __tablename__ = "workspace"

    id: Mapped[UUID] = mapped_column(primary_key=True)

    def __init__(self, id: UUID) -> None:
       self.id = id

    items: Mapped[list["DbItem"]] = relationship(back_populates="workspace")
    members: Mapped[list["DbWorkspaceMember"]] = relationship(back_populates="workspace")


class DbUser(DbBase):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    firebase_auth_uid: Mapped[str]
    email: Mapped[str]

    def __init__(self, id: UUID, firebase_auth_uid: str, email: str) -> None:
        self.id = id
        self.firebase_auth_uid = firebase_auth_uid
        self.email = email

    workspace_memberships: Mapped[list["DbWorkspaceMember"]] = relationship(back_populates="user")


class DbWorkspaceMember(DbBase):
    __tablename__ = "workspace_member"

    workspace_id: Mapped[UUID] = mapped_column(ForeignKey("workspace.id"))
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))

    def __init__(self, workspace_id: UUID, user_id: UUID):
        self.workspace_id = workspace_id
        self.user_id = user_id

    workspace: Mapped["DbWorkspace"] = relationship(back_populates="members")
    user: Mapped["DbUser"] = relationship(back_populates="workspace_memberships")
    created_items: Mapped[list["DbItem"]] = relationship(back_populates="creator")


class DbItem(DbBase):
    __tablename__ = "item"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    title: Mapped[str]
    text_content: Mapped[str]

    def __init__(self, id: UUID, title: str, text_content: str, last_modification_datetime: datetime):
        self.id = id
        self.title = title
        self.text_content = text_content
        self.last_modification_datetime = last_modification_datetime

    last_modification_datetime: Mapped[datetime]

    workspace_id: Mapped[UUID] = mapped_column(ForeignKey("workspace.id"))
    creator_id: Mapped[UUID] = mapped_column(ForeignKey("workspace_member.id"))

    workspace: Mapped["DbWorkspace"] = relationship(back_populates="items")
    creator: Mapped["DbWorkspaceMember"] = relationship(back_populates="created_items")
