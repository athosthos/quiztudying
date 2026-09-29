from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class Response(Base):
    __tablename__ = "tbl_resposta"

    __table_args__ = (
        UniqueConstraint(
            "id_tentativa_pergunta",
            name="uq_tbl_resposta_tentativa_pergunta"
        ),
    )

    id_resposta: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    dt_inicio: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    dt_fim: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    id_alternativa: Mapped[int] = mapped_column(
        ForeignKey("tbl_alternativa.id_alternativa"),
        nullable=False
    )

    id_tentativa_pergunta: Mapped[int] = mapped_column(
        ForeignKey("tbl_tentativa_pergunta.id_tentativa_pergunta"),
        nullable=False
    )