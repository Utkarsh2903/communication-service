from __future__ import annotations

import enum


class ChannelType(enum.Enum):
    WHATSAPP = "whatsapp"
    EMAIL = "email"
    SMS = "sms"
    IVR = "ivr"
    APP_NOTIFICATION = "app_notification"


class Status(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
