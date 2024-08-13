from __future__ import annotations

from contextlib import contextmanager

from fastapi.logger import logger
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.app_config import DB_URL

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine,
                            expire_on_commit=False)
Base = declarative_base()


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = SessionLocal()  # Create a new session
    try:
        yield session  # Provide the session to the caller
        session.commit()  # Commit the transaction if no exceptions
    except Exception:
        session.rollback()  # Rollback in case of an exception
        raise  # Re-raise the exception
    finally:
        session.close()  # Ensure the session is closed after use


def connect_to_db():
    session = SessionLocal()
    try:
        session.execute(text("SELECT 1"))
        logger.info("Database connection successful")
    finally:
        session.close()


def shutdown():
    logger.info("Closing database session")
    session = SessionLocal()
    session.close()
