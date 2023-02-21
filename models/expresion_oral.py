from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class ExpresiOnoral(Base):
    __tablename__ = "expresion_oral"

    id_expresion_oral = Column(Integer, primary_key=True, index=True)
    observaciones = Column(String)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntos_conseguidos = Column(Integer, nullable=False, default=0)
    puntuacion_maxima_parte = Column(Integer, nullable=False, default=0)
    tarea_1 = relationship("Tarea", back_populates="id_tarea")
    tarea_2 = relationship("Tarea", back_populates="id_tarea")
