from __future__ import annotations

from fastapi import APIRouter

from src.schemas.request.gateway_schema import CreateGatewayRequestSchema
from src.schemas.request.gateway_schema import UpdateGatewayRequestSchema
from src.services.gateway_service import GatewayService

router = APIRouter()


@router.post("/", summary="Create a gateway")
async def create_gateway(request: CreateGatewayRequestSchema):
    gateway = GatewayService()
    return gateway.create(request.model_dump())


@router.get("/{gateway_id}", summary="Get a gateway")
async def get_gateway(gateway_id: int):
    gateway = GatewayService()
    return gateway.get(gateway_id)


@router.patch("/{gateway_id}", summary="Update a gateway")
async def update_gateway(gateway_id: int, request: UpdateGatewayRequestSchema):
    gateway = GatewayService()
    return gateway.update(gateway_id, request.model_dump())


@router.delete("/{gateway_id}", summary="Delete a gateway")
async def delete_gateway(gateway_id: int):
    gateway = GatewayService()
    return gateway.delete(gateway_id)
