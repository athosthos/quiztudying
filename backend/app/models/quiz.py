from datetime import datetime
from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class Quiz(Base):
    __tablename__ = "tbl_quiz"

    __table_args__ = (
        CheckConstraint(
            """
            nr_tempo_limite IS NULL
            OR nr_tempo_limite BETWEEN 1 AND 60
            """,
            name="ck_tbl_quiz_nr_tempo_limite"
        ),
    )

    id_quiz: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nm_quiz: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    ds_quiz: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    is_ativo: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="true"
    )

    is_publico: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false"
    )

    is_ordem_aleatoria: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false"
    )

    is_distribuicao_automatica: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="true"
    )

    nr_tempo_limite: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    dt_criacao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    dt_publicacao: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("tbl_usuario.id_usuario"),
        nullable=False
    )

    id_idioma: Mapped[int] = mapped_column(
        ForeignKey("tbl_idioma.id_idioma"),
        nullable=False
    )