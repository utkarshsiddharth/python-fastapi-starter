from pydantic import BaseModel, Field, EmailStr

# -------- User Schema --------
class UserBase(BaseModel):
    email: str
    is_active: bool
    

class CreateUserDto(BaseModel):
    email: EmailStr = Field(title="User Email", description="User Email") 
    password: str = Field(title="Password", description="Password with length greater than equal to 8",min_length=8)
class UpdateUserDto(BaseModel):
    is_active: bool

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

class User(UserBase):
    password: str

class LoginDto(BaseModel):
    email: str 
    password: str
     