from typing import List
from api.api_model import ApiItem, ApiItemData, ApiUserDataSnapshot, ApiUserInfo
from model.model import Item, User, UserData


def to_api_item_snippet(item: Item) -> ApiItem:
    return ApiItem(
        uri=item.uri,
        data=ApiItemData(title=item.title, text_content=item.text_content),
        last_modification_date=item.last_modification_date,
    )


def to_api_user_info(user: User) -> ApiUserInfo:
    return ApiUserInfo(uri=user.uri)


def to_api_user_data_snapshot(user_data: UserData) -> ApiUserDataSnapshot:
    items: List[ApiItem] = [to_api_item_snippet(i) for w in user_data.workspaces_data for i in w.items]
    return ApiUserDataSnapshot(userInfo=to_api_user_info(user_data.user), items=items)
