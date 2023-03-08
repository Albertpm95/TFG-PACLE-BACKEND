from pydantic import BaseModel


class Alumno(BaseModel):
    nombre: str
    apellidos: str
    dni: str
    id_alumno: int

    class Config:
        orm_mode = True
