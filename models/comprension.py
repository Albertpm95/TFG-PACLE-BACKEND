from sqlalchemy import Column, ForeignKey, Integer, String

from db.database import Base


class Comprension(Base):
    __tablename__ = "comprension"

    id_acta = Column(Integer, ForeignKey("actas.id_acta"))
    id_comprension = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    observaciones = Column(String)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntos_conseguidos = Column(Integer, nullable=False, default=0)
    puntuacion_maxima_parte = Column(Integer, nullable=False, default=0)
    puntuacion_tarea_1 = Column(Integer, nullable=False, default=0)
    puntuacion_tarea_2 = Column(Integer, nullable=False, default=0)
    puntuacion_tarea_3 = Column(Integer, nullable=False, default=0)
