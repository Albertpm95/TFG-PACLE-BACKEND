from typing import Literal
from pydantic import BaseModel


class UsuarioBase(BaseModel):
    username: str


class UsuarioLogin(UsuarioBase):
    password: str


class Usuario(UsuarioBase):
    id: int
    username: str
    nombre: str
    apellidos: str
    password: str
    is_active: bool
    rol: Literal['Admin', 'Gestor', 'Corrector']
