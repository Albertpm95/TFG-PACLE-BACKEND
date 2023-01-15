from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    nombre: str
    apellido: str
    usuario: str
    password: str


class Admin(User):
    rol = 'Admin'


class Gestor(User):
    rol = 'Gestor'


class Corrector(User):
    rol = 'Corrector'
