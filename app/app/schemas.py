from pydantic import BaseModel

class CounterBase(BaseModel):
    count: int

class Counter(CounterBase):
    id: int

    class Config:
        orm_mode = True

class CounterCreate(CounterBase):
    pass
