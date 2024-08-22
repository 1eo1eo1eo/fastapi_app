from core.models import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import TIMESTAMP


class Operation(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[str] = mapped_column()
    figi: Mapped[str] = mapped_column()
    instrument_type: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[TIMESTAMP] = mapped_column(type_=TIMESTAMP)
    type: Mapped[str] = mapped_column()