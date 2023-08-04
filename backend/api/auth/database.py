from datetime import datetime
from typing import Optional

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import TIMESTAMP, Column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"
    # birthdate = Column(TIMESTAMP, default=datetime.utcnow())
