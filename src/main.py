from __future__ import annotations

from fastapi import FastAPI

from config.database import connect_to_db
from config.database import shutdown
from src.routers.account_router import router as account_router
from src.routers.gateway_configuration_router import router as gateway_configuration_router
from src.routers.gateway_router import router as gateway_router
from src.routers.sender_router import router as sender_router

app = FastAPI()


@app.on_event("startup")
def startup_func():
    connect_to_db()


@app.on_event("shutdown")
def shutdown_func():
    shutdown()


@app.get('/')
def read_root():
    return {"Hello": "World"}


app.include_router(account_router, prefix='/accounts')
app.include_router(gateway_router, prefix='/gateways')
app.include_router(gateway_configuration_router,
                   prefix='/gateway-configurations')
app.include_router(sender_router, prefix='/senders')
