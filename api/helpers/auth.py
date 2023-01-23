from fastapi import Depends,HTTPException
import jwt
from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from api.schemas.user_schema import UserOut
from api.models.user_model import UserModel
from api.helpers.db_helpers import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
from api.db.database import SessionLocal
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SECRET_KEY = 'nuclearcodesforfastapi'
ALGORITHM = 'HS256'

def current_user_scheme(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> UserOut:
    """ decode the token """
    user = decode_token(db=db, Model=UserModel,token=token)
    return user
    
def encode_token(payload, expires_delta: timedelta = None):
    payload_to_encode = payload.copy()

    if expires_delta:
        expires_in = datetime.utcnow() + expires_delta
    else:
        expires_in = datetime.utcnow() + timedelta(minutes=15)
    payload_to_encode.update({'exp': expires_in})
    encoded_jwt = jwt.encode(payload_to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(db, Model, token) -> UserOut:
    credentials_exception = HTTPException(
   	status_code=401,
   	detail="Could not validate credentials",
   )

    """ decode token"""
    try:
        print(token)
        payload: UserOut = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise credentials_exception
    except: 
        raise credentials_exception
    """ Get user by email """
    user: UserOut = find_item_by_email(db, Model, email)
    if user is None:
        raise HTTPException(status_code=404, details='User Not Found!!')
    return user