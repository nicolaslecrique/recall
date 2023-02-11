from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, MetaData
from sqlalchemy.orm import declarative_base

DbBase = declarative_base(metadata=MetaData(schema="recall_db_schema"))


class DbWorkspace(DbBase):
    __tablename__ = "workspace"

    id: Mapped[int] = mapped_column(primary_key=True)
    uri: Mapped[str]

    items: Mapped[list["DbItem"]] = relationship(back_populates="workspace")
    members: Mapped[list["DbWorkspaceMember"]] = relationship(back_populates="workspace")


class DbUser(DbBase):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    uri: Mapped[str]
    firebase_auth_uid: Mapped[str]
    email: Mapped[str]

    workspace_memberships: Mapped[list["DbWorkspaceMember"]] = relationship(back_populates="user")


class DbWorkspaceMember(DbBase):
    __tablename__ = "workspace_member"

    id: Mapped[int] = mapped_column(primary_key=True)
    workspace_id: Mapped[int] = mapped_column(ForeignKey("workspace.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    workspace: Mapped["DbWorkspace"] = relationship(back_populates="members")
    user: Mapped["DbUser"] = relationship(back_populates="workspace_memberships")
    created_items: Mapped[list["DbItem"]] = relationship(back_populates="creator")


class DbItem(DbBase):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(primary_key=True)
    uri: Mapped[str]
    title: Mapped[str]
    text_content: Mapped[str]
    last_modification_datetime: Mapped[datetime]

    workspace_id: Mapped[int] = mapped_column(ForeignKey("workspace.id"))
    creator_id: Mapped[int] = mapped_column(ForeignKey("workspace_member.id"))

    workspace: Mapped["DbWorkspace"] = relationship(back_populates="items")
    creator: Mapped["DbWorkspaceMember"] = relationship(back_populates="created_items")
