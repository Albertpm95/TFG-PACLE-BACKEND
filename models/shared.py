from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.alumno import Alumno
    from models.convocatoria import Convocatoria


class AlumnosConvocatoria(SQLModel, table=True):
    __tablename__: str = "alumnos_convocatoria"

    id: Optional[int] = Field(default=None, primary_key=True)
    idConvocatoria: int = Field(foreign_key="convocatorias.idConvocatoria")
    idAlumno: int = Field(foreign_key="alumnos.idAlumno")
    convocatoria: "Convocatoria" = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Convocatoria.idConvocatoria==AlumnosConvocatoria.idConvocatoria",
            "lazy": "joined",
        },
        back_populates="alumnos_matriculados",
    )
    alumno: "Alumno" = Relationship(
        sa_relationship_kwargs={"primaryjoin": "Alumno.idAlumno==AlumnosConvocatoria.idAlumno", "lazy": "joined"},
        back_populates="convocatorias_matriculadas",
    )
