from pydantic import BaseModel


class AlumnoBase(BaseModel):
    name: str


class AlumnoCreate(AlumnoBase):
    pass


class Alumno(AlumnoBase):
    id_alumno: int
    id_convocatoria: int

    class Config:
        orm_mode = True
        orm_name = "AlumnoSQL"


class ConvocatoriaBase(BaseModel):
    name: str


class ConvocatoriaCreate(ConvocatoriaBase):
    pass


class Convocatoria(ConvocatoriaBase):
    id_convocatoria: int
    alumnos: list[Alumno] = []

    class Config:
        orm_mode = True
        orm_name = "ConvocatoriaSQL"
