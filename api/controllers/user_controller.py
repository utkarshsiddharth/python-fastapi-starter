
from api.schemas.user_schema import User

userDB = []

async def get_all_users_c() -> dict:
    return {
        "users": userDB
    }
    

async def get_user_by_id_c(user_id: int):
    item = None
    for iteration, user in enumerate(userDB):
        if user['id'] == user_id:
            item = user
            break
    
    if item is None:
        return {
            "status": "error",
            "message": "User not found"
        }
    
    return {
        "status": "OK",
        "user": user
    }

async def create_user_c(user: User) -> dict:
    item = {
        "email": user.email,
        "password": user.password,
    }
    item['id'] = len(userDB) + 1
    userDB.append(item)
    return {
        "status": "OK",
        "user": item
    } 

