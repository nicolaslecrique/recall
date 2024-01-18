from typing import Optional
import uuid

from db.db_service import DbService
from model.model import User, UserData, Workspace, WorkspaceData


class CrudService:
    db: DbService = DbService()

    def get_or_create_user(self, firebase_auth_ui: str, email: str) -> UserData:
        user_data: Optional[UserData] = self.db.get_user_data(firebase_auth_ui)
        if user_data is not None:
            return user_data
        else:
            user = User(firebase_auth_ui, uuid.uuid4(), email)
            workspace = Workspace(uuid.uuid4())
            self.db.create_user_and_workspace(user, workspace)
            return UserData(user, [WorkspaceData(workspace, [])])
