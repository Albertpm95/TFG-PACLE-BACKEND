from pydantic import BaseModel


class Idioma(BaseModel):
    id_lenguaje: int
    lenguaje: str

    class Config:
        orm_mode = True
