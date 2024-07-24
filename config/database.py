from __future__ import annotations

from fastapi.logger import logger
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.app_config import DB_URL

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine,
                            expire_on_commit=False)
Base = declarative_base()


def connect_to_db():
    session = SessionLocal()
    try:
        yield session
        logger.info("Database connection successful")
    finally:
        session.close()


def shutdown():
    logger.info("Closing database session")
    session = SessionLocal()
    session.close()
