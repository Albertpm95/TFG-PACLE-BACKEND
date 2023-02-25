from pydantic import BaseModel

from constants import ROLES


class Rol(BaseModel):
    id_rol: int
    rol: ROLES

    class Config:
        orm_mode = True
