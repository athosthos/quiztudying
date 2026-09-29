from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class QuizCategory(Base):
    __tablename__ = "tbl_quiz_categoria"

    id_quiz: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("tbl_quiz.id_quiz"),
        primary_key=True
    )

    id_categoria: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("tbl_categoria.id_categoria"),
        primary_key=True
    )