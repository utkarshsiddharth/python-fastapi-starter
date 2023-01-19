from fastapi import FastAPI
from api.schemas.product_schema import *
from api.schemas.user_schema import *
from api.controllers.user_controller import *

app = FastAPI()

# User Routes

# Get All Users
@app.get('/users')
async def get_all_users() -> list[User]:
    return await get_all_users_c()

# Get User By User ID
@app.get('/users/{user_id}')
async def get_user_by_id(user_id: int) -> dict:
    return await get_user_by_id_c(user_id)

# Create a new user
@app.post('/users')
async def create_user(user: CreateUserDto) -> dict:
    return await create_user_c(user) 

# Update user by User ID
@app.put('/users/{user_id}')
async def update_user_by_id(user_id: int, user: UpdateUserDto) -> dict:
    return await update_user_by_id_c(user_id, user)

# Delete user by User ID
@app.delete('/users/{user_id}')
async def delete_user_by_id(user_id: int):
    return await delete_user_by_id_c(user_id)

# Post Routes 

