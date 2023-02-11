from typing import Optional

from db.db_service import DbService
from model.model import User, UserData, Workspace, WorkspaceData
from tools.uri_utils import generate_uri


class CrudService:
    db: DbService = DbService()

    def get_or_create_user(self, firebase_auth_ui: str, email: str) -> UserData:
        user_data: Optional[UserData] = self.db.get_user_data(firebase_auth_ui)
        if user_data is not None:
            return user_data
        else:
            user_uri: str = generate_uri(email)
            user = User(firebase_auth_ui, user_uri, email)
            workspace = Workspace(generate_uri(f"default_{user_uri}"))
            self.db.create_user_and_workspace(user, workspace)
            return UserData(user, [WorkspaceData(workspace, [])])
