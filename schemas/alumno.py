from pydantic import BaseModel


class AlumnoBase(BaseModel):
    nombre: str
    apellidos: str
    dni: str
    id_alumno: int

    class Config:
        orm_mode = True


class AlumnoActa(AlumnoBase):
    class Config:
        orm_mode = True
