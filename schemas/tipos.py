from pydantic import BaseModel


class Tipos(BaseModel):
    tipo: str

    class Config:
        orm_mode = True
