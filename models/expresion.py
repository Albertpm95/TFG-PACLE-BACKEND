from sqlalchemy import Column, ForeignKey, Integer, String

from db.base_class import Base

class Expresion(Base):
    __tablename__ = "expresion"

    id_expresion = Column(String, nullable=False, primary_key=True)
    observaciones = Column(String)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntos_conseguidos = Column(Integer, nullable=False, default=0)
    puntuacion_maxima_parte = Column(Integer, nullable=False, default=0)
    tarea_1 = Column(String, ForeignKey("Pacle_db.tarea.id_tarea"), nullable=False)
    tarea_2 = Column(String, ForeignKey("Pacle_db.tarea.id_tarea"), nullable=False)
    id_acta = Column(String, ForeignKey("Pacle_db.actas.id_acta"), nullable=False)
