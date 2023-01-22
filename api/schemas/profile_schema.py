from pydantic import BaseModel, Field, EmailStr
from api.schemas.user_schema import UserOut

# -------- Profile Schema ----------
class ProfileBase(BaseModel):
    first_name: str 
    last_name: str
    country: str
    
class Profile(ProfileBase): 
    id: int 
    user_id: int 
    user: UserOut
    class Config:
        orm_mode = True

class CreateProfileDto(BaseModel):
    first_name: str = Field(title='First Name', description='Your First Name')
    last_name: str = Field(title='Last Name', description='Your Last Name')
    country: str = Field(title='Country Name', description='Your Country Name') 
    user_id: int = Field(title='User ID', description='Your User ID')

class UpdateProfileDto(BaseModel):
    first_name: str 
    last_name: str 
    country: str