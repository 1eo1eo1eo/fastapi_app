from .base import Base

from sqlalchemy import JSON
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped


class Role(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    permissions: Mapped[JSON] = mapped_column(type_=JSON)