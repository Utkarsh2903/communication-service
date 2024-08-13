from __future__ import annotations

import yaml

filepath = "config/env.yml"
with open(filepath) as f:
    settings = yaml.safe_load(f)
    DB_URL = settings.get("db_url")
    REDIS_URL = settings.get("redis_url")
    ENCRYPTION_KEY = settings.get("encryption_key")
