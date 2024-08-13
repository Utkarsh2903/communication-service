from __future__ import annotations

from config.database import session_scope
from src.models.sender import Sender


class SenderService:

    def __init__(self) -> None:
        pass

    def create(self, sender):
        created_sender = Sender(**sender)
        with session_scope() as session:
            session.add(created_sender)
        return created_sender

    def get(self, sender_id: int):
        with session_scope() as session:
            return session.query(Sender).filter(Sender.id == sender_id).first()

    def update(self, sender_id: int, sender):
        db_sender = self.get(sender_id)
        if db_sender:
            for key, value in sender.items():
                setattr(db_sender, key, value)
            with session_scope() as session:
                session.add(db_sender)
        return db_sender

    def delete(self, sender_id: int):
        db_sender = self.get(sender_id)
        if db_sender:
            with session_scope() as session:
                session.delete(db_sender)
        return db_sender
