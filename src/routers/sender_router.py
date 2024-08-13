from __future__ import annotations

from fastapi import APIRouter

from src.schemas.request.sender_schema import CreateSenderRequestSchema
from src.schemas.request.sender_schema import UpdateSenderRequestSchema
from src.services.sender_service import SenderService

router = APIRouter()


@router.post("/", summary="Create a sender")
async def create_sender(request: CreateSenderRequestSchema):
    sender = SenderService()
    return sender.create(request.model_dump())


@router.get("/{sender_id}", summary="Get a sender")
async def get_sender(sender_id: int):
    sender = SenderService()
    return sender.get(sender_id)


@router.patch("/{sender_id}", summary="Update a sender")
async def update_sender(sender_id: int, request: UpdateSenderRequestSchema):
    sender = SenderService()
    return sender.update(sender_id, request.model_dump())


@router.delete("/{sender_id}", summary="Delete a sender")
async def delete_sender(sender_id: int):
    sender = SenderService()
    return sender.delete(sender_id)
