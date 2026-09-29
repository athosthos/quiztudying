from datetime import datetime
from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class Attempt(Base):
    __tablename__ = "tbl_tentativa"

    __table_args__ = (
        CheckConstraint(
            "nr_questoes > 0",
            name="ck_tbl_tentativa_nr_questoes"
        ),
    )

    id_tentativa: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    dt_inicio: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    dt_limite: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    dt_fim: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    nr_questoes: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    id_quiz: Mapped[int] = mapped_column(
        ForeignKey("tbl_quiz.id_quiz"),
        nullable=False
    )

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("tbl_usuario.id_usuario"),
        nullable=False
    )

    ds_status: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )