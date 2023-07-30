from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from api.auth.database import Base, User

import os
from dotenv import load_dotenv

load_dotenv()

#DATABASE_URL = "postgresql+asyncpg://mishka_user:QAgI0tO1dAARZiBgm9yLxlqpw6ZTESON@dpg-cj1aras07spjv9rk4d80-a.frankfurt-postgres.render.com/mishka"
DATABASE_URL = os.environ.get('DATABASE_URL') 



engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)