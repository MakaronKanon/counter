from fastapi import FastAPI, Body, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/counters/", response_model=schemas.Counter)
def create_counter(counter: schemas.CounterCreate, db: Session = Depends(get_db)):
    return crud.create_counter(db, counter)


@app.get("/counters/{counter_id}", response_model=schemas.Counter)
def read_counter(counter_id: int, db: Session = Depends(get_db)):
    counter = crud.get_counter(db, counter_id=counter_id)
    if counter is None:
        raise HTTPException(status_code=404, detail="Counter not found")
    return counter

# @app.put("/counters")
# def update_counter(counter: int = Body(..., embed=True)):
#     # Todo: set counter.
#     return counter

