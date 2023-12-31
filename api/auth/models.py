from datetime import datetime

from sqlalchemy import (JSON, TIMESTAMP, UUID, Column, ForeignKey, Integer,
                        MetaData, String, Table)

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("roles.id")),
)
