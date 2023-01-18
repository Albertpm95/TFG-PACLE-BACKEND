from pydantic import BaseModel


class AlumnoBase(BaseModel):
    name: str


class AlumnoCreate(AlumnoBase):
    pass


class Alumno(AlumnoBase):
    id_alumno: int
    id_convocatoria: int
