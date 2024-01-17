from typing import Optional, List

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from db.db_converters import to_user, to_item, to_workspace
from model.model import UserData, Workspace, WorkspaceData, User
from recall.recall_back.db.db_model import DbItem, DbUser, DbWorkspace, DbWorkspaceMember


class DbService:
    engine = create_engine(
        "postgresql://recall_server_db_user:recall_server_db_user_test_pwd@localhost:5432/postgres",
        echo=True,
    )

    def get_user_data(self, firebase_auth_uid: str) -> Optional[UserData]:
        user_query = select(DbUser).where(DbUser.firebase_auth_uid == firebase_auth_uid)
        with Session(self.engine) as session:
            db_user: Optional[DbUser] = session.scalar(user_query)
            if db_user is None:
                return None
            else:
                workspace_memberships: List[DbWorkspaceMember] = db_user.workspace_memberships
                workspaces_data: List[WorkspaceData] = []
                for db_workspace_member in workspace_memberships:
                    db_workspace: DbWorkspace = db_workspace_member.workspace
                    db_items: list[DbItem] = db_workspace.items
                    workspace_data = WorkspaceData(
                        workspace=to_workspace(db_workspace),
                        items=[to_item(i) for i in db_items],
                    )
                    workspaces_data.append(workspace_data)
                return UserData(user=to_user(db_user), workspaces_data=workspaces_data)

    def create_user_and_workspace(self, user: User, workspace: Workspace):
        with Session(self.engine) as session:
            db_workspace = DbWorkspace(id=workspace.id)
            db_user = DbUser(firebase_auth_uid=user.firebase_auth_uid, id=user.id, email=user.email)
            session.add(db_workspace)
            session.add(db_user)
            session.flush()
            db_workspace_member = DbWorkspaceMember(workspace_id=db_workspace.id, user_id=db_user.id)
            session.add(db_workspace_member)
            session.commit()
