from __future__ import annotations

from config.database import session_scope
from src.models.gateway import Gateway


class GatewayService:

    def __init__(self) -> None:
        pass

    def create(self, gateway):
        created_gateway = Gateway(**gateway)
        with session_scope() as session:
            session.add(created_gateway)
        return created_gateway

    def get(self, gateway_id: int):
        with session_scope() as session:
            return session.query(Gateway).filter(
                Gateway.id == gateway_id).first()

    def update(self, gateway_id: int, gateway):
        db_gateway = self.get(gateway_id)
        if db_gateway:
            for key, value in gateway.items():
                setattr(db_gateway, key, value)
            with session_scope() as session:
                session.add(db_gateway)
        return db_gateway

    def delete(self, gateway_id: int):
        db_gateway = self.get(gateway_id)
        if db_gateway:
            with session_scope() as session:
                session.delete(db_gateway)
        return db_gateway
