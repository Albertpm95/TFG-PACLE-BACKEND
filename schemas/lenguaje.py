from pydantic import BaseModel


class LenguajeBase(BaseModel):
    lenguaje: str

    class Config:
        orm_mode = True


class Lenguaje(LenguajeBase):
    idLenguaje: int

    class Config:
        orm_mode = True
