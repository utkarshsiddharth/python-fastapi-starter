from sqlalchemy.orm import Session
from api.schemas.user_schema import User
from fastapi import HTTPException

def find_item_by_id(db: Session, Model, id: int):
    item = db.query(Model).filter(Model.id == id).first()
    if item is None:
        raise HTTPException(status_code=404, detail='Profile not found')
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