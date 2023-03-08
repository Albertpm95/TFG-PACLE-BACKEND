from sqlalchemy import Column, Integer, String, ForeignKey, null

from db.database import Base


class Expresion(Base):
    __tablename__ = "expresion"

    id_expresion = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    observaciones = Column(String)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntos_conseguidos = Column(Integer, nullable=False, default=0)
    puntuacion_maxima_parte = Column(Integer, nullable=False, default=0)
    tarea_1 = Column(Integer, ForeignKey("tarea.id_tarea"))
    tarea_2 = Column(Integer, ForeignKey("tarea.id_tarea"))
