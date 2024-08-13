from __future__ import annotations

from config.database import session_scope
from src.models.account import Account


class AccountService:

    def __init__(self) -> None:
        pass

    def create(self, account):
        created_account = Account(**account)
        with session_scope() as session:
            session.add(created_account)
        return created_account

    def get(self, account_id: int):
        with session_scope() as session:
            return session.query(Account).filter(
                Account.id == account_id).first()

    def update(self, account_id: int, account):
        db_account = self.get(account_id)
        if db_account:
            for key, value in account.items():
                setattr(db_account, key, value)
            with session_scope() as session:
                session.add(db_account)
        return db_account

    def delete(self, account_id: int):
        db_account = self.get(account_id)
        if db_account:
            with session_scope() as session:
                session.delete(db_account)
        return db_account
