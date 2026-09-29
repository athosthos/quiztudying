from datetime import datetime
from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class Evaluation(Base):
    __tablename__ = "tbl_avaliacao"

    __table_args__ = (
        CheckConstraint(
            "nr_nota BETWEEN 1 AND 5",
            name="ck_tbl_avaliacao_nr_nota"
        ),
    )

    id_avaliacao: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nr_nota: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    dt_avaliacao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    id_quiz: Mapped[int] = mapped_column(
        ForeignKey("tbl_quiz.id_quiz"),
        nullable=False
    )

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("tbl_usuario.id_usuario"),
        nullable=False
    )