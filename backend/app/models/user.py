from datetime import datetime
from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class User(Base):
    __tablename__ = "tbl_usuario"

    __table_args__ = (
        UniqueConstraint(
            "nm_usuario",
            name="uq_tbl_usuario_nm_usuario"
        ),
    )

    id_usuario: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nm_usuario: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    ds_senha_hash: Mapped[str] = mapped_column(
        String(255),
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

    id_idioma: Mapped[int] = mapped_column(
        ForeignKey("tbl_idioma.id_idioma"),
        nullable=False
    )