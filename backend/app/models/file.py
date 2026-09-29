from datetime import datetime
from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class File(Base):
    __tablename__ = "tbl_arquivo"

    __table_args__ = (
        CheckConstraint(
            "nr_questoes IS NULL OR nr_questoes > 0",
            name="ck_tbl_arquivo_nr_questoes"
        ),
    )

    id_arquivo: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nm_arquivo: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    uri_arquivo: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    tp_arquivo: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    nr_questoes: Mapped[int | None] = mapped_column(
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

    id_quiz: Mapped[int] = mapped_column(
        ForeignKey("tbl_quiz.id_quiz"),
        nullable=False
    )