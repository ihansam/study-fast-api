from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class MacBookSpec(Base):
    __tablename__ = 'macbook_spec'

    pid = Column(Integer, primary_key=True, autoincrement=True)
    pname = Column(String(255), nullable=False)
    processor = Column(String(255))
    display = Column(Float)
    unpack = Column(Integer)
