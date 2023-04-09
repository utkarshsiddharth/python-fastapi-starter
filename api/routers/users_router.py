from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from api.injectables.user_injectable import current_user_scheme

# User Schema
from api.schemas.user_schema import *
# User Controller
from api.controllers.user_controller import *

router = APIRouter(
prefix='/users',
tags = ['users']
)

# Get All Users
@router.get('/')
async def get_all_users(db: Session = Depends(get_db)):
    return await get_all_users_c(db=db)

# Get current logged in user
@router.get('/me', response_model=UserOut)
async def get_current_user(user: UserOut = Depends(current_user_scheme)):
    return user

# Get User By User ID
@router.get('/{user_id}')
async def get_user_by_id(user_id: int,db: Session = Depends(get_db)) -> UserOut:
    return await get_user_by_id_c(db, user_id)


# Create a new user
@router.post('/')
async def create_user(user: CreateUserDto, db: Session = Depends(get_db)) -> UserOut:
    return await create_user_c(db=db, user=user) 


# Login user with email and password
@router.post('/login')
async def login(login_input: LoginDto, db: Session = Depends(get_db)):
    token = await login_c(db=db, login_input=login_input)
    content = {
        "access_token": token,
        "token_type": "bearer"
    }
    response = JSONResponse(content)
    response.set_cookie("auth_token", token)
    return response


# protected - (admin or self) - Update User by User ID 
@router.put('/{user_id}')
async def update_user_by_id(user_id: int, user: UpdateUserDto, db: Session = Depends(get_db)) -> UserOut:
    return await update_user_by_id_c(db=db,user_id=user_id, user=user)



# protected - (admin or self) - Delete a User by User ID
@router.delete('/{user_id}')
async def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return await delete_user_by_id_c(db=db, user_id=user_id)


# public
@router.post('/activate')
async def activate_user_account(data: UserActivateToken, db: Session = Depends(get_db)):
    return await activate_user_account_c(db=db, data=data)



    
