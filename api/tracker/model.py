from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String, Float, Boolean
from sqlalchemy.orm import relationship

from user.model import User

Base = declarative_base()

class Entry_Type(Base):
    __tablename__='entry_type'
    entry_type = Column(String, primary_key=True, index=True)
    has_description = Column(Boolean, nullable=False)
    has_amount = Column(Boolean, nullable=False)
    created_at = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey(User.id))

# backref: https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html
class Entry(Base):
    __tablename__='entry'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    amount = Column(Float)
    created_at = Column(Float, nullable=False)
    entry_type = Column(String, ForeignKey('entry_type.entry_type'))
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User,backref='entries')