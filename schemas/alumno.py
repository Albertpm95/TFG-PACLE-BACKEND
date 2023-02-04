from pydantic import BaseModel


class AlumnoBase(BaseModel):
    nombre: str
    apellidos: str


class Alumno(AlumnoBase):
    id: str
    examinado_convocatoria: str

    class Config:
        orm_mode = True
