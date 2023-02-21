from sqlalchemy import Column, DateTime, Integer, String

from db.database import Base


class Convocatoria(Base):
    __tablename__ = "convocatorias"

    comprension_auditiva_puntuacion_maxima_parte = Column(
        Integer(), nullable=False, default=0
    )
    comprension_lectora_puntuacion_maxima_parte = Column(
        Integer(), nullable=False, default=0
    )
    expresion_escrita_puntuacion_maxima_parte = Column(
        Integer(), nullable=False, default=0
    )
    expresion_oral_puntuacion_maxima_parte = Column(
        Integer(), nullable=False, default=0
    )
    id_convocatoria = Column(Integer, primary_key=True, index=True)
    lenguaje = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    fecha = Column(DateTime, nullable=False)
