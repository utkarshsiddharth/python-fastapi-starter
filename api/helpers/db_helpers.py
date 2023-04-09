from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from fastapi import HTTPException

from sqlalchemy.orm import Session
from api.schemas.user_schema import LoginDto,UserOut
from api.utils.utils import *
from api.models.user_model import UserModel

from api.models.user_model import Base
from api.db.database import SessionLocal, engine
Base.metadata.create_all(bind=engine)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def find_item_by_id(db: Session, Model, id: int):
    item = db.query(Model).filter(Model.id == id).first()
    return item

def find_item_by_email(db: Session, Model: UserModel, email: str):
    item = db.query(Model).filter(Model.email == email).first()
    return item

def find_item_by_email(db: Session, Model, email: str):
    item = db.query(Model).filter(Model.email == email).first()
    return item

# Authenticate user
def authenticate_user(db: Session, Model, login_input: LoginDto) -> UserOut | bool:
    """ Check if user exists """
    item = find_item_by_email(db, Model=Model, email=login_input.email)
    if item is None:
        return False
    
    """ Check if user account is active """
    if item.is_active == False:
        raise HTTPException(status_code=403, detail="Please activate your account before logging in")



    """ Check if password is correct """
    match = verify_password(plain_password=login_input.password, hashed_password=item.password)
    
    if match is False:
        return False
    return item


def find_item_by_id_and_update(db: Session, Model, id: int, payload):
    db_item_query = db.query(Model).filter(Model.id == id)
    db_item = db_item_query.first()

    update_item = payload.dict(exclude_unset=True)
    db_item_query.filter(Model.id == id).update(update_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def find_by_id_and_remove(db: Session, Model, id: int) -> bool:
    db.query(Model).filter(Model.id == id).delete()
    db.commit()
    return True

# Login 

def verify_password(plain_password, hashed_password):
   return pwd_context.verify(plain_password, hashed_password)
 
def get_password_hash(password):
   return pwd_context.hash(password)
