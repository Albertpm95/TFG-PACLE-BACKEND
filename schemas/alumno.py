from pydantic import BaseModel


class Alumno(BaseModel):
    nombre: str
    apellidos: str
    dni: str

    class Config:
        orm_mode = True


class AlumnoDB(Alumno):
    id_alumno: int

    class Config:
        orm_mode = True
