from __future__ import annotations

from pydantic import BaseModel

from src.models.enum import Status


class CreateAccountRequestSchema(BaseModel):
    name: str
    sub_tenant_id: int
    status: Status


class UpdateAccountRequestSchema(BaseModel):
    name: str
    sub_tenant_id: int
    status: Status
