
from api.schemas.user_schema import *
from api.helpers.user_helpers import find_user_by_user_id
from api.helpers.helpers import * 

userDB = []

# Get all Users
async def get_all_users_c() -> list[User]:
    return userDB
    
# Get user by User ID
async def get_user_by_id_c(user_id: int) -> dict:
    user = find_user_by_user_id(userDB, user_id)
    if user is None:
        return {
            "status": "error",
            "message": "User not found"
        }
    return {
        "status": "OK",
        "user": user
    }

# Create a new User
async def create_user_c(user: CreateUserDto) -> dict:
    item = {
        "email": user.email,
        "password": user.password,
        "name": user.name
    }
    item['id'] = len(userDB) + 1
    userDB.append(item)
    return {
        "status": "OK",
        "user": item
    }
    
# Update User by User ID 
async def update_user_by_id_c(user_id: int, user: UpdateUserDto):
    item = find_user_by_user_id(userDB, user_id)
    if item is None:
        return {
            "status": "error",
            "message": "User not found"
        }

    return item.update(user)
    

# Delete a User by User ID
async def delete_user_by_id_c(user_id: int):
    itemIndex = find_index(userDB, 'id', user_id)
    print(itemIndex, 'found item to delete ...')
    if itemIndex < 0:
        return {
            "status": "error",
            "message": "User not found"
        }
    # remove the user 
    del userDB[itemIndex]
    return userDB


