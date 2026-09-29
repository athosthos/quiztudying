from datetime import datetime
from sqlalchemy import (
    Boolean,
    DateTime,
    Integer,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class Language(Base):
    __tablename__ = "tbl_idioma"

    __table_args__ = (
        UniqueConstraint(
            "cd_idioma",
            name="uq_tbl_idioma_cd_idioma"
        ),
    )

    id_idioma: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nm_idioma: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    cd_idioma: Mapped[str] = mapped_column(
        String(10),
        nullable=False
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