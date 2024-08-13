from __future__ import annotations

from pydantic import BaseModel

from src.models.enum import Status


class CreateGatewayConfigurationRequestSchema(BaseModel):
    name: str
    account_id: int
    gateway_id: int
    configuration_details: dict
    status: Status


class UpdateGatewayConfigurationRequestSchema(BaseModel):
    name: str
    account_id: int
    gateway_id: int
    configuration_details: dict
    status: Status
