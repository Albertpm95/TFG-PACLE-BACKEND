from pydantic import BaseModel


class Tipos(BaseModel):
    id_tipo: int
    tipo: str

    class Config:
        orm_mode = True
