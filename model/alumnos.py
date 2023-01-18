from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base


class Alumno(Base):
    __tablename__ = "alumnos"

    id_alumno = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    id_convocatoria = Column(Integer, ForeignKey("convocatorias.id_convocatoria"))

    owner = relationship("Convocatoria", back_populates="items")
