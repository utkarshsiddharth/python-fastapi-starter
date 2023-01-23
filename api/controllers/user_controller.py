
from sqlalchemy.orm import Session
from api.schemas.user_schema import *
from api.helpers.db_helpers import *
from api.helpers.helpers import * 
from api.models.user_model import *
from api.utils.utils import *
from api.helpers.auth import *

from fastapi import HTTPException

# Get all Users
async def get_all_users_c(db: Session):
    return db.query(UserModel).all()
    
# Get user by User ID
async def get_user_by_id_c(db: Session, user_id: int) -> UserOut:
    user = find_item_by_id(db=db,Model=UserModel, id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user

# Create a new User
async def create_user_c(db: Session, user: CreateUserDto) -> UserOut:
    hashed_password = get_password_hash(user.password)
    db_user = UserModel(password=hashed_password, email=user.email, is_active=False)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    
# protected - (admin or self) - Update User by User ID 
async def update_user_by_id_c(db: Session, user_id: int, user: UpdateUserDto):
    item = find_item_by_id(db,Model=UserModel, id=user_id)
    if item is None:
        raise HTTPException('User Not Found!!')
    updated_item = find_item_by_id_and_update(db=db, Model=UserModel, id=user_id,payload=user)
    return updated_item
    

# protected - (admin or self) - Delete a User by User ID
async def delete_user_by_id_c(db: Session, user_id: int):
    item = find_item_by_id(db,Model=UserModel, id=user_id)
    if item is None:
        raise HTTPException('User Not Found!!')
    is_removed = find_by_id_and_remove(db=db, Model=UserModel, id=user_id)
    if is_removed:
        return 'User Removed Sucessfully!!'
    return 'Something went wrong while removing user'

# Login user by email 
async def login_c(db: Session, login_input: LoginDto):
    authenticated = authenticate_user(db=db, Model=UserModel, login_input=login_input)
    if authenticated is None or authenticated is False:
        raise HTTPException(status_code=400, detail='Invalid Credentials')
    print(authenticated, 'authenticated')
    user: UserOut = authenticated
    """ sing a JWT token"""
    payload = {
        'sub': user.email,
    }
    token = encode_token(payload=payload)
    return token

