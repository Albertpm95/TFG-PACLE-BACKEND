from pydantic import BaseModel


class AlumnoBase(BaseModel):
    nombre: str
    apellidos: str
    dni: str

    class Config:
        orm_mode = True


class AlumnoActa(AlumnoBase):
    class Config:
        orm_mode = True
