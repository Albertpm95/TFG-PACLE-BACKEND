from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from db.database import Base

from models.tarea import Tarea


class ExpresionOral(Base):
    __tablename__ = "expresion_oral"

    idExpresion = Column(Integer, primary_key=True, unique=True)
    observaciones = Column(String)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntos_conseguidos = Column(Integer, nullable=False, default=0)
    puntuacion_maxima_parte = Column(Integer, nullable=False, default=0)
    idTarea = Column(Integer, ForeignKey("tareas.idTarea"))
    tareas: Mapped[Tarea] = relationship()
