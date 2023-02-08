from pydantic import BaseModel


class AlumnoBase(BaseModel):
    id: str
    nombre: str
    apellidos: str


class Alumno(AlumnoBase):

    examinado_convocatoria: str

    class Config:
        orm_mode = True
