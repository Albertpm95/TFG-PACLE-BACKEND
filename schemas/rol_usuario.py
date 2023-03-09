from typing import Optional
from pydantic import BaseModel


class Rol(BaseModel):
    id_rol: int
    rol: Optional[str]

    class Config:
        orm_mode = True
