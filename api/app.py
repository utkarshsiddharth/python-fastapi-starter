from fastapi import FastAPI, Depends
from api.schemas.user_schema import *
from api.schemas.profile_schema import *
from api.controllers.user_controller import *
from api.controllers.profile_controller import *
from api.models.user_model import Base
from api.db.database import SessionLocal, engine
from api.utils.docs import tags_metadata
from api.helpers.auth import current_user_scheme


Base.metadata.create_all(bind=engine)
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

app = FastAPI(openapi_tags=tags_metadata)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -- User Routes -- #

# Get All Users
@app.get('/users',tags=['users'])
async def get_all_users(db: Session = Depends(get_db)):
    return await get_all_users_c(db=db)

# Get current logged in user
@app.get('/users/me',tags=['users'], response_model=UserOut)
async def get_current_user(user: UserOut = Depends(current_user_scheme)):
    return user

# Get User By User ID
@app.get('/users/{user_id}',tags=['users'])
async def get_user_by_id(user_id: int,db: Session = Depends(get_db)) -> UserOut:
    return await get_user_by_id_c(db, user_id)


# Create a new user
@app.post('/users',tags=['users'])
async def create_user(user: CreateUserDto, db: Session = Depends(get_db)) -> UserOut:
    return await create_user_c(db=db, user=user) 

@app.post('/token')
async def get_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    login_input = LoginDto(email=form_data.username,password=form_data.password)
    token = await login_c(db=db,login_input=login_input)
    return {
        "access_token": token,
        "token_type": "bearer"
    }


# Login user with email and password
@app.post('/users/login',tags=['users'])
async def login(login_input: LoginDto, db: Session = Depends(get_db)):
    return await login_c(db=db, login_input=login_input)


# protected - (admin or self) - Update User by User ID 
@app.put('/users/{user_id}',tags=['users'])
async def update_user_by_id(user_id: int, user: UpdateUserDto, db: Session = Depends(get_db)) -> UserOut:
    return await update_user_by_id_c(db=db,user_id=user_id, user=user)



# protected - (admin or self) - Delete a User by User ID
@app.delete('/users/{user_id}',tags=['users'])
async def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return await delete_user_by_id_c(db=db, user_id=user_id)



    

# -- Profile Routes -- #

# protected - (admin or self) - Get All Profiles
@app.get('/profile',tags=['profile'],response_model=list[Profile])
async def get_all_profiles(db: Session = Depends(get_db)) -> list[Profile]:
    return await get_all_profiles_c(db=db)


# protected - (admin or self) - Get Profile By User ID
@app.get('/profile/{profile_id}',tags=['profile'])
async def get_profile_by_id(profile_id: int,db: Session = Depends(get_db)) -> Profile:
    return await get_profile_by_id_c(db, profile_id)

# protected - (admin or self) - Create Profile
@app.post('/profile',tags=['profile'])
async def create_profile(profile: CreateProfileDto, db: Session = Depends(get_db)) -> Profile:
    return await create_profile_c(db=db, profile=profile) 

# protected - (admin or self) - Update profile by User ID
@app.put('/profile/{profile_id}',tags=['profile'])
async def update_profile_by_id(profile_id: int, profile: UpdateProfileDto, db: Session = Depends(get_db)) -> Profile:
    return await update_profile_by_id_c(db=db,profile_id=profile_id, profile=profile)

# protected - (admin or self) - Delete profile by profile ID
@app.delete('/profile/{user_id}',tags=['profile'])
async def delete_profile_by_id(profile_id: int,db: Session = Depends(get_db)):
    return await delete_profile_by_id_c(db=db, profile_id=profile_id)


