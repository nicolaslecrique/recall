from typing import List
from api.api_model import ApiItem, ApiUserDataSnapshot, ApiUserInfo
from model.model import Item, User, UserData


def to_api_item_snippet(item: Item) -> ApiItem:
    return ApiItem(id=item.id, title=item.title, text_content=item.text_content, last_modification_date=item.last_modification_date)


def to_api_user_info(user: User) -> ApiUserInfo:
    return ApiUserInfo(id=user.id)


def to_api_user_data_snapshot(user_data: UserData) -> ApiUserDataSnapshot:
    items: List[ApiItem] = [to_api_item_snippet(i) for w in user_data.workspaces_data for i in w.items]
    return ApiUserDataSnapshot(userInfo=to_api_user_info(user_data.user), items=items)
