from pydantic import BaseModel


class GeneroBase(BaseModel):
    genero: str

    class Config:
        orm_mode = True


class Genero(GeneroBase):
    idGenero: int

    class Config:
        orm_mode = True
