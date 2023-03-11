from pydantic import BaseModel


class Lenguaje(BaseModel):
    id_lenguaje: int
    lenguaje: str

    class Config:
        orm_mode = True
