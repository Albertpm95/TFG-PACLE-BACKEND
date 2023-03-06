from pydantic import BaseModel


class Tipo(BaseModel):
    id_tipo: int
    tipo: str

    class Config:
        orm_mode = True
