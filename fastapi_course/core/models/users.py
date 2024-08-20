from .base import Base

import datetime
from sqlalchemy import TIMESTAMP, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped


class Users(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    registered_at: Mapped[TIMESTAMP] = mapped_column(type_=TIMESTAMP, default=datetime.UTC)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))