from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Convocatoria(Base):
    __tablename__ = "pacle_db.convocatorias"

    id_convocatoria = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    alumnos = relationship("Alumno", back_populates="owner")


class Alumno(Base):
    __tablename__ = "pacle_db.alumnos"

    id_alumno = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    id_convocatoria = Column(Integer, ForeignKey(
        "pacle_db.convocatorias.id_convocatoria"))

    owner = relationship("Convocatoria", back_populates="alumnos")
