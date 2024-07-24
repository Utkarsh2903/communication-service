from __future__ import annotations

from fastapi import FastAPI

from config.database import connect_to_db
from config.database import shutdown

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
