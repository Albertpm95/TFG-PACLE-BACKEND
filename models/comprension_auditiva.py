from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from db.database import Base


class ComprensionAuditiva(Base):
    __tablename__ = "comprension_auditiva"

    id_comprension_auditiva = Column(Integer, primary_key=True, index=True)

    observaciones = Column(String)
    porcentaje = Column(Integer, nullable=False, default=0)
    puntos_conseguidos = Column(Integer, nullable=False, default=0)
    puntuacion_maxima_parte = Column(Integer, nullable=False, default=0)
    puntuacion_tarea_1 = Column(Integer, nullable=False, default=0)
    puntuacion_tarea_2 = Column(Integer, nullable=False, default=0)
    puntuacion_tarea_3 = Column(Integer, nullable=False, default=0)
