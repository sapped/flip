from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String, Float, Date, Boolean

Base = declarative_base()

class Goal(Base):
    __tablename__ = 'goals'
    id = Column(Integer, primary_key=True, index=True)
    goal = Column(String, nullable=False, unique=True)
    has_amount = Column(Boolean, nullable=False)
    date_created = Column(Date, nullable=False)

class Entry(Base):
    __tablename__ = 'entries'
    
    id = Column(Integer, primary_key=True, index=True)
    goal_id = Column(Integer, ForeignKey('goals.id'), nullable=False)
    date = Column(Date, nullable=False)
    tracked = Column(Boolean, nullable=False)
    amount = Column(Float, nullable=True)