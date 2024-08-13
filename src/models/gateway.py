from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint

from config.database import Base
from src.models.enum import ChannelType
from src.models.enum import Status


class Gateway(Base):
    __tablename__ = 'gateways'
    UNIQUE_COLUMNS = ['id', 'name']

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    channel_type = Column(Enum(ChannelType), nullable=False)
    status = Column(Enum(Status), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime,
                        nullable=False,
                        default=datetime.now,
                        onupdate=datetime.now)

    __table_args__ = (UniqueConstraint('name',
                                       'channel_type',
                                       name='uq_name_channel_type'),)
