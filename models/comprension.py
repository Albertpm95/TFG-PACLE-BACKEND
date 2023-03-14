
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base


class Comprension(Base):
    __tablename__ = "comprension"

    id_comprension = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    observaciones = Column(String)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntos_conseguidos = Column(Integer, nullable=False, default=0)
    puntuacion_maxima_parte = Column(Integer, nullable=False, default=0)

    __table_args__ = (
        UniqueConstraint("id_comprension", "tipo", name="acta_comprension_unique"),
    )
