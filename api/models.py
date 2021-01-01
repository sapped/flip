from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, Boolean

Base = declarative_base()

class Tracker(Base):
    __tablename__ = 'tracker'
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    crossfit = Column(Boolean)
    gowod = Column(Boolean)
    yoga = Column(Boolean)
    weight = Column(Float)
    calories = Column(Integer)