from pydantic import BaseModel


class RolBase(BaseModel):
    rol: str

    class Config:
        orm_mode = True


class Rol(RolBase):
    idRol: int

    class Config:
        orm_mode = True
