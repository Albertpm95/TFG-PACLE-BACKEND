from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, null
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.database import Base


class Expresion(Base):
    __tablename__ = "expresion"

    id_expresion = Column(Integer, primary_key=True, unique=True)
    tipo = Column(String)
    observaciones = Column(String)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntos_conseguidos = Column(Integer, nullable=False, default=0)
    puntuacion_maxima_parte = Column(Integer, nullable=False, default=0)
    tarea_1 = Column(Integer, ForeignKey("tarea.id_tarea"))
    tarea_2 = Column(Integer, ForeignKey("tarea.id_tarea"))
    __table_args__ = (
        UniqueConstraint("id_expresion", "tipo", name="acta_expresion_unique"),
    )
