from api.schemas.user_schema import User


def find_user_by_user_id(userDB: list, user_id: int) -> User | None:
    print(user_id, 'find_user_by_user_id')
    item = None
    for user in userDB:
        print(user)
        if user['id'] == user_id:
            item = user
            break
    return item

