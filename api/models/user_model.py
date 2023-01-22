from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.db.database import Base

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True,index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean)
    profile = relationship('ProfileModel', back_populates='user')

class ProfileModel(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True,index=True)
    first_name = Column(String)
    last_name = Column(String)
    profile_pic = Column(String)
    country = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('UserModel', back_populates='profile')
    
