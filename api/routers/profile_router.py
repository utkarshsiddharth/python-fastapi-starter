from fastapi import APIRouter, Depends

# Profile Schema
from api.schemas.profile_schema import *
# Profile Controller
from api.controllers.profile_controller import *

router = APIRouter(
prefix='/profile',
tags = ['profile']
)


# protected - (admin or self) - Get All Profiles
@router.get('/profile',response_model=list[Profile])
async def get_all_profiles(db: Session = Depends(get_db)) -> list[Profile]:
    return await get_all_profiles_c(db=db)


# protected - (admin or self) - Get Profile By User ID
@router.get('/profile/{profile_id}')
async def get_profile_by_id(profile_id: int,db: Session = Depends(get_db)) -> Profile:
    return await get_profile_by_id_c(db, profile_id)

# protected - (admin or self) - Create Profile
@router.post('/profile')
async def create_profile(profile: CreateProfileDto, db: Session = Depends(get_db)) -> Profile:
    return await create_profile_c(db=db, profile=profile) 

# protected - (admin or self) - Update profile by User ID
@router.put('/profile/{profile_id}')
async def update_profile_by_id(profile_id: int, profile: UpdateProfileDto, db: Session = Depends(get_db)) -> Profile:
    return await update_profile_by_id_c(db=db,profile_id=profile_id, profile=profile)

# protected - (admin or self) - Delete profile by profile ID
@router.delete('/profile/{user_id}')
async def delete_profile_by_id(profile_id: int,db: Session = Depends(get_db)):
    return await delete_profile_by_id_c(db=db, profile_id=profile_id)
