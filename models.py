from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
Base.metadata.schema = 'Pacle_db'


class Convocatoria(Base):
    __tablename__ = "convocatorias"

    id_convocatoria = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    alumnos = relationship("Alumno", back_populates="owner")


class Alumno(Base):
    __tablename__ = "alumnos"

    id_alumno = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    id_convocatoria = Column(Integer, ForeignKey(Convocatoria.id_convocatoria))

    owner = relationship("Convocatoria", back_populates="alumnos")
