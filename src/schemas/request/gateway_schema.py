from __future__ import annotations

from pydantic import BaseModel

from src.models.enum import ChannelType
from src.models.enum import Status


class CreateGatewayRequestSchema(BaseModel):
    name: str
    channel_type: ChannelType
    status: Status


class UpdateGatewayRequestSchema(BaseModel):
    name: str
    channel_type: ChannelType
    status: Status
