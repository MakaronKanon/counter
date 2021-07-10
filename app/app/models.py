from sqlalchemy import Integer, Column

from .database import Base

class Counter(Base):
    __tablename__ = "counters"

    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer)

