from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel

#  we are creating a class - To convert this class into a model we inherit a base class from ORM
Base = declarative_base()
# declarative base returns our base class from ORM as output
class Task(Base):
    __tablename__ = "task"
    task_id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(255),nullable=False)
    staus = Column(Boolean,default=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)


