from sqlalchemy import (
    CheckConstraint,
    ForeignKey,
    Integer,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class AttemptQuestion(Base):
    __tablename__ = "tbl_tentativa_pergunta"

    __table_args__ = (
        UniqueConstraint(
            "id_tentativa",
            "id_pergunta",
            name="uq_tbl_tentativa_pergunta_pergunta"
        ),
        UniqueConstraint(
            "id_tentativa",
            "nr_ordem",
            name="uq_tbl_tentativa_pergunta_ordem"
        ),
        CheckConstraint(
            "nr_ordem > 0",
            name="ck_tbl_tentativa_pergunta_nr_ordem"
        ),
    )

    id_tentativa_pergunta: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    id_tentativa: Mapped[int] = mapped_column(
        ForeignKey("tbl_tentativa.id_tentativa"),
        nullable=False
    )

    id_pergunta: Mapped[int] = mapped_column(
        ForeignKey("tbl_pergunta.id_pergunta"),
        nullable=False
    )

    nr_ordem: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )