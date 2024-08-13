from __future__ import annotations

from pydantic import BaseModel

from src.models.enum import Status


class CreateSenderRequestSchema(BaseModel):
    name: str
    gateway_configuration_id: int
    sender_details: dict
    status: Status


class UpdateSenderRequestSchema(BaseModel):
    name: str
    gateway_configuration_id: int
    sender_details: dict
    status: Status
