from pydantic import BaseModel


class AlumnoBase(BaseModel):
    id_alumno: str
    nombre: str
    apellidos: str
    dni: str

    class Config:
        orm_mode = True


class AlumnoActa(AlumnoBase):
    class Config:
        orm_mode = True
