from pydantic import BaseModel


class Genero(BaseModel):
    idGenero: int
    genero: str

    class Config:
        orm_mode = True
