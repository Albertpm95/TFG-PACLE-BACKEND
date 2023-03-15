from pydantic import BaseModel


class Lenguaje(BaseModel):
    idLenguaje: int
    lenguaje: str

    class Config:
        orm_mode = True
