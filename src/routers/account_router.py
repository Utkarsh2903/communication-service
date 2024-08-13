from __future__ import annotations

from fastapi import APIRouter

from src.schemas.request.account_schema import CreateAccountRequestSchema
from src.schemas.request.account_schema import UpdateAccountRequestSchema
from src.services.account_service import AccountService

router = APIRouter()


@router.post("/", summary="Create an account")
async def create_account(request: CreateAccountRequestSchema):
    account = AccountService()
    return account.create(request.model_dump())


@router.get("/{account_id}", summary="Get an account")
async def get_account(account_id: int):
    account = AccountService()
    return account.get(account_id)


@router.patch("/{account_id}", summary="Update an account")
async def update_account(account_id: int, request: UpdateAccountRequestSchema):
    account = AccountService()
    return account.update(account_id, request.model_dump())


@router.delete("/{account_id}", summary="Delete an account")
async def delete_account(account_id: int):
    account = AccountService()
    return account.delete(account_id)
