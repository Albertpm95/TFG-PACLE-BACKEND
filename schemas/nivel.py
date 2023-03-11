from pydantic import BaseModel


class Nivel(BaseModel):
    id_nivel: int
    nivel: str

    class Config:
        orm_mode = True
