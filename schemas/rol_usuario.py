from pydantic import BaseModel


class Rol(BaseModel):
    rol: str

    class Config:
        orm_mode = True
