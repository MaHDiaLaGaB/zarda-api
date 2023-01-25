from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Base
from typing import Generator
import logging


class DataBase:

    def __init__(self) -> None:
        self._engine = create_engine(
            "sqlite:///database.db",
            connect_args={"check_same_thread": False},
            echo=True,
        )
        self._session_factory = sessionmaker(bind=self._engine)
        self.db_session: Session = self._session_factory()
        self._engine.connect()
        Base.metadata.create_all(self._engine)

    def session(self) -> Generator[int, None, None]:
        try:
            yield self.db_session
        except Exception:
            logging.exception("session rollback")
            self.db_session.rollback()
            raise
        finally:
            self.db_session.close()


