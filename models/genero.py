from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

class Genero(SQLModel, table=True):
    __tablename__: str = "generos"

    idGenero: Optional[int] = Field(default=None, primary_key=True)
    genero: str = Field(nullable=False, unique=True)

    #idAlumno: Optional[int] = Field(foreign_key="alumnos.idAlumno")
    #alumno: Optional[list[Alumno]] = Relationship(back_populates="genero")