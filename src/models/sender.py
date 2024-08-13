from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import String

from config.database import Base
from src.models.enum import Status


class Sender(Base):
    __tablename__ = 'senders'
    UNIQUE_COLUMNS = ['id']

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gateway_configuration_id = Column(Integer,
                                      ForeignKey('gateway_configurations.id'),
                                      nullable=False)
    sender_details = Column(JSON, nullable=False)
    status = Column(Enum(Status), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime,
                        nullable=False,
                        default=datetime.now,
                        onupdate=datetime.now)
