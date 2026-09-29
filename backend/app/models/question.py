from datetime import datetime
from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    Text,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class Question(Base):
    __tablename__ = "tbl_pergunta"

    __table_args__ = (
        CheckConstraint(
            """
            is_ativo = false
            OR nr_ordem IS NOT NULL
            """,
            name="ck_tbl_pergunta_ordem_ativa"
        ),
    
        CheckConstraint(
            "nr_ordem IS NULL OR nr_ordem > 0",
            name="ck_tbl_pergunta_nr_ordem_positiva"
        ),
    
        Index(
            "uq_tbl_pergunta_quiz_nr_ordem_ativo",
            "id_quiz",
            "nr_ordem",
            unique=True,
            postgresql_where=text("is_ativo = true")
        ),
    )

    id_pergunta: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    ds_pergunta: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    nr_ordem: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    is_ativo: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="true"
    )

    dt_criacao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    ds_explicacao: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    id_quiz: Mapped[int] = mapped_column(
        ForeignKey("tbl_quiz.id_quiz"),
        nullable=False
    )