from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class ExpresionEscrita(Base):
    __tablename__ = "expresion_escrita"

    id_expresion_escrita = Column(Integer, primary_key=True, index=True)
    observaciones = Column(String)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntos_conseguidos = Column(Integer, nullable=False, default=0)
    puntuacion_maxima_parte = Column(Integer, nullable=False, default=0)
    id_tarea_1 = Column(Integer, ForeignKey("tarea.id_tarea"))
    id_tarea_2 = Column(Integer, ForeignKey("tarea.id_tarea"))
