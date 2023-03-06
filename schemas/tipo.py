from pydantic import BaseModel


class Tipo(BaseModel):
    tipo: str

    class Config:
        orm_mode = True
