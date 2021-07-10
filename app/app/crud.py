from sqlalchemy.orm import Session

from . import models, schemas

def get_counter(db: Session, counter_id: int):
    return db.query(models.Counter).filter(models.Counter.id == counter_id).first()

def create_counter(db: Session, counter: schemas.CounterCreate):
    db_item = models.Counter(**counter.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

