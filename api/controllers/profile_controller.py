
from sqlalchemy.orm import Session
from api.schemas.profile_schema import *
from api.helpers.db_helpers import *
from api.helpers.helpers import * 
from api.models.user_model import *

# protected - (admin or self) - Get All Profiles
async def get_all_profiles_c(db: Session) -> list[Profile]:
    return db.query(ProfileModel).all()
    
# protected - (admin or self) - Get Profile By profile ID
async def get_profile_by_id_c(db: Session, profile_id: int) -> Profile:
    profile = find_item_by_id(db=db,Model=ProfileModel, id=profile_id)
    return profile

# protected - (admin or self) - Create Profile
async def create_profile_c(db: Session, profile: CreateProfileDto) -> Profile:
    db_profile = ProfileModel(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
    
# protected - (admin or self) - Update profile by profile ID
async def update_profile_by_id_c(db: Session, profile_id: int, profile: UpdateProfileDto):
    item = find_item_by_id(db,Model=UserModel, id=profile_id)
    if item is None:
        raise HTTPException('Profile Not Found!!')
    updated_item = find_item_by_id_and_update(db=db, Model=ProfileModel, id=profile_id,payload=profile)
    return updated_item

# protected - (admin or self) - Delete profile by profile ID
async def delete_profile_by_id_c(db: Session, profile_id: int):
    item = find_item_by_id(db,Model=UserModel, id=profile_id)
    if item is None:
        raise HTTPException('Profile Not Found!!')
    is_removed = find_by_id_and_remove(db=db, Model=ProfileModel, id=profile_id)
    if is_removed:
        return 'Profile Removed Sucessfully!!'
    return 'Something went wrong while removing profile'


