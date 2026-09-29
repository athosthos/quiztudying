from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Index, Integer, Text, func, text
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class Alternative(Base):
    __tablename__ = "tbl_alternativa"

    __table_args__ = (
        Index(
            "uq_tbl_alternativa_pergunta_correta_ativa",
            "id_pergunta",
            unique=True,
            postgresql_where=text(
                "is_ativo = true AND is_correto = true"
            )
        ),
    )

    id_alternativa: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    ds_alternativa: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    is_ativo: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="true"
    )

    is_correto: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    dt_criacao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    id_pergunta: Mapped[int] = mapped_column(
        ForeignKey("tbl_pergunta.id_pergunta"),
        nullable=False
    )