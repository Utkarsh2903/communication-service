from __future__ import annotations

from fastapi import APIRouter

from src.schemas.request.gateway_configuration_schema import CreateGatewayConfigurationRequestSchema
from src.schemas.request.gateway_configuration_schema import UpdateGatewayConfigurationRequestSchema
from src.services.gateway_configuration_service import GatewayConfigurationService

router = APIRouter()


@router.post("/", summary="Create a gateway configuration")
async def create_gateway_configuration(
        request: CreateGatewayConfigurationRequestSchema):
    gateway_configuration = GatewayConfigurationService()
    return gateway_configuration.create(request.model_dump())


@router.get("/{gateway_configuration_id}",
            summary="Get a gateway configuration")
async def get_gateway_configuration(gateway_configuration_id: int):
    gateway_configuration = GatewayConfigurationService()
    return gateway_configuration.get(gateway_configuration_id)


@router.patch("/{gateway_configuration_id}",
              summary="Update a gateway configuration")
async def update_gateway_configuration(
        gateway_configuration_id: int,
        request: UpdateGatewayConfigurationRequestSchema):
    gateway_configuration = GatewayConfigurationService()
    return gateway_configuration.update(gateway_configuration_id,
                                        request.model_dump())


@router.delete("/{gateway_configuration_id}",
               summary="Delete a gateway configuration")
async def delete_gateway_configuration(gateway_configuration_id: int):
    gateway_configuration = GatewayConfigurationService()
    return gateway_configuration.delete(gateway_configuration_id)
