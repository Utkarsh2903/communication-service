from __future__ import annotations

from config.database import session_scope
from src.models.gateway_configuration import GatewayConfiguration


class GatewayConfigurationService:

    def __init__(self) -> None:
        pass

    def create(self, gateway_configuration):
        created_gateway_configuration = GatewayConfiguration(
            **gateway_configuration)
        with session_scope() as session:
            session.add(created_gateway_configuration)
        return created_gateway_configuration

    def get(self, gateway_configuration_id: int):
        with session_scope() as session:
            return session.query(GatewayConfiguration).filter(
                GatewayConfiguration.id == gateway_configuration_id).first()

    def update(self, gateway_configuration_id: int, gateway_configuration):
        db_gateway_configuration = self.get(gateway_configuration_id)
        if db_gateway_configuration:
            for key, value in gateway_configuration.items():
                setattr(db_gateway_configuration, key, value)
            with session_scope() as session:
                session.add(db_gateway_configuration)
        return db_gateway_configuration

    def delete(self, gateway_configuration_id: int):
        db_gateway_configuration = self.get(gateway_configuration_id)
        if db_gateway_configuration:
            with session_scope() as session:
                session.delete(db_gateway_configuration)
        return db_gateway_configuration
