from fastapi import Depends, Response, Cookie
from api.helpers.auth import decode_token
from api.models.user_model import UserModel
from api.schemas.user_schema import UserOut
from api.helpers.db_helpers import get_db
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def current_user_scheme(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> UserOut:
    """ decode the token """
    user = decode_token(db=db, Model=UserModel,token=token)
    return user
