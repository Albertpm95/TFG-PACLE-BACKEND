from pydantic import BaseModel


class Idioma(BaseModel):
    lenguaje: str

    class Config:
        orm_mode = True
