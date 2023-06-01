
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from models.alumno import Alumno
from models.convocatoria import Convocatoria


class AlumnosConvocatoria(SQLModel, table=True):
    __tablename__: str = "alumnos_convocatoria"

    id: Optional[int] = Field(default=None, primary_key=True)
    idConvocatoria: int = Field(foreign_key="convocatorias.idConvocatoria")
    idAlumno: int = Field(foreign_key="alumnos.idAlumno")
    convocatoria: Convocatoria = Relationship(sa_relationship_kwargs={"primaryjoin": "Convocatoria.idConvocatoria==AlumnosConvocatoria.idConvocatoria", "lazy": "joined"})
    alumno: Alumno = Relationship(sa_relationship_kwargs={"primaryjoin": "Alumno.idAlumno==AlumnosConvocatoria.idAlumno", "lazy": "joined"})

"""
class AlumnosActa(SQLModel, table=True):
    __tablename__ = "alumnos_acta"

    id: Optional[int] = Field(default=None, primary_key=True)
    idActa: int = Field(foreign_key="actas.idActa")
    idAlumno: int = Field(foreign_key="alumnos.idAlumno")
    acta: Acta = Relationship(sa_relationship_kwargs={"primaryjoin": "Acta.idActa==AlumnosActa.idActa", "lazy": "joined"})
    alumno: Alumno = Relationship(sa_relationship_kwargs={"primaryjoin": "Alumno.idAlumno==AlumnosActa.idAlumno", "lazy": "joined"})
    
class ActaCompresion(SQLModel, table=True):
    __tablename__ = "comprensiones_acta"

    id: Optional[int] = Field(default=None, primary_key=True)
    idComprension: int = Field(nullable=False, foreign_key="comprensiones.idComprension")
    acta: Acta = Relationship(sa_relationship_kwargs={"primaryjoin": "Acta.idActa==ActaCompresion.idActa", "lazy": "joined"})
    idActa: int = Field(nullable=False, foreign_key="actas.idActa")
    acta: Acta = Relationship(sa_relationship_kwargs={"primaryjoin": "Acta.idActa==ActaCompresion.idActa", "lazy": "joined"})


class ActaExpresion(SQLModel, table=True):
    __tablename__ = "expresiones_acta"

    id: Optional[int] = Field(default=None, primary_key=True)
    idExpresion: int = Field(nullable=False, foreign_key="expresiones.idExpresion")
    acta: Expresion = Relationship(sa_relationship_kwargs={"primaryjoin": "Expresion.idExpresion==ActaExpresion.idExpresion", "lazy": "joined"})
    idActa: int = Field(nullable=False, foreign_key="actas.idActa")
    acta: Acta = Relationship(sa_relationship_kwargs={"primaryjoin": "Acta.idActa==ActaExpresion.idActa", "lazy": "joined"})
"""
