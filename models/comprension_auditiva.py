from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from db.database import Base

from models.tarea import Tarea


class ComprensionAuditiva(Base):
    __tablename__ = "comprension_auditiva"

    idComprension = Column(Integer, primary_key=True)
    observaciones = Column(String)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntos_conseguidos = Column(Integer, nullable=False, default=0)
    puntuacion_maxima_parte = Column(Integer, nullable=False, default=0)
    idTarea = Column(Integer, ForeignKey("tareas.idTarea"))
    tareas: Mapped[Tarea] = relationship()
    