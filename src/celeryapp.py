# src/config/celery.py
from __future__ import annotations

from celery import Celery

from config.app_config import REDIS_URL

# Initialize Celery with RabbitMQ as the broker and backend
celery_app = Celery(
    "communication_service",
    broker=REDIS_URL,  # Change this to your RabbitMQ URL
    backend=REDIS_URL)

# Celery configuration
celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
)
