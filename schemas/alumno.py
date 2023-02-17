from pydantic import BaseModel


class AlumnoBase(BaseModel):
    id_alumno: str
    nombre: str
    apellidos: str
    dni: str


class AlumnoActa(AlumnoBase):
    id_acta: str

    class Config:
        orm_mode = True
