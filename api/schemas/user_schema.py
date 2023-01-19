from pydantic import BaseModel 

class User(BaseModel):
    id: str
    name: str
    email: str 
    password: str

class CreateUserDto(BaseModel):
    name: str
    email: str 
    password: str

class UpdateUserDto(BaseModel):
    name: str