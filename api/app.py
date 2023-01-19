from fastapi import FastAPI
from api.schemas.product_schema import *
from api.controllers.user_controller import *

app = FastAPI()

@app.get('/users')
async def get_all_users() -> dict:
    return await get_all_users_c()

@app.get('/users/{user_id}')
async def get_user_by_id(user_id: int):
    return await get_user_by_id_c(user_id)

@app.post('/users')
async def create_user(user: User):
    return await create_user_c(user) 
