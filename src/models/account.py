from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import event
from sqlalchemy import Integer
from sqlalchemy import String

from config.database import Base
from src.models.enum import Status


class Account(Base):
    __tablename__ = 'accounts'
    UNIQUE_COLUMNS = ['id', 'name', 'api_key']

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    sub_tenant_id = Column(Integer, nullable=False)
    api_key = Column(String, nullable=False, unique=True)
    status = Column(Enum(Status), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime,
                        nullable=False,
                        default=datetime.now,
                        onupdate=datetime.now)


"""
A function that generates an API key before an Account object is inserted into the database.
"""


@event.listens_for(Account, "before_insert")
def generate_api_key(mapper, connection, target):
    target.api_key = str(uuid.uuid4())
