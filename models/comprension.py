from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class Comprension(Base):
    __tablename__ = "comprension"

    id_comprension = Column(Integer, primary_key=True, index=True)
    observaciones = Column(String)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntos_conseguidos = Column(Integer, nullable=False, default=0)
    puntuacion_maxima_parte = Column(Integer, nullable=False, default=0)
    puntuacion_tarea_1 = Column(Integer, nullable=False, default=0)
    puntuacion_tarea_2 = Column(Integer, nullable=False, default=0)
    puntuacion_tarea_3 = Column(Integer, nullable=False, default=0)
    id_acta = Column(Integer, ForeignKey("actas.id_acta"))
    tipo = Column(String, nullable=False)

    acta = relationship("Acta", back_populates="comprensiones")
