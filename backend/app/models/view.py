from datetime import datetime
from uuid import UUID
from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID as PostgreSQLUUID
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class View(Base):
    __tablename__ = "tbl_visualizacao"

    __table_args__ = (
        CheckConstraint(
            """
            (id_usuario IS NOT NULL AND id_visitante IS NULL)
            OR
            (id_usuario IS NULL AND id_visitante IS NOT NULL)
            """,
            name="ck_tbl_visualizacao_usuario_visitante"
        ),
        Index(
            "ix_tbl_visualizacao_id_visitante",
            "id_visitante"
        ),
    )

    id_visualizacao: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    dt_visualizacao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    id_usuario: Mapped[int | None] = mapped_column(
        ForeignKey("tbl_usuario.id_usuario"),
        nullable=True
    )

    id_visitante: Mapped[UUID | None] = mapped_column(
        PostgreSQLUUID(as_uuid=True),
        nullable=True,
    )

    id_quiz: Mapped[int] = mapped_column(
        ForeignKey("tbl_quiz.id_quiz"),
        nullable=False
    )