from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import event
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import String
from sqlalchemy import UniqueConstraint

from config.database import Base
from src.models.enum import Status
from src.utils.crypto import CryptoManager

KEYS_TO_ENCRYPT = ['api_key']


class GatewayConfiguration(Base):
    __tablename__ = 'gateway_configurations'
    UNIQUE_COLUMNS = ['id', 'name']

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    gateway_id = Column(Integer, ForeignKey('gateways.id'), nullable=False)
    configuration_details = Column(JSON, nullable=False)
    status = Column(Enum(Status), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime,
                        nullable=False,
                        default=datetime.now,
                        onupdate=datetime.now)

    __table_args__ = (UniqueConstraint('name',
                                       'account_id',
                                       'gateway_id',
                                       name='uq_name_account_id_gateway_id'),)


@event.listens_for(GatewayConfiguration, "before_insert")
@event.listens_for(GatewayConfiguration, "before_update")
def encrypt_keys(mapper, connection, target):
    for key in KEYS_TO_ENCRYPT:
        if key in target.configuration_details:
            target.configuration_details[key] = CryptoManager().encrypt(
                target.configuration_details[key])


@event.listens_for(GatewayConfiguration, "load")
def decrypt_keys(target, context):
    for key in KEYS_TO_ENCRYPT:
        if key in target.configuration_details:
            target.configuration_details[key] = CryptoManager().decrypt(
                target.configuration_details[key])
