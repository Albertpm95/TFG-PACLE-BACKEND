from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[str]
    username: str


class UserDB(User):
    password: str


class Admin(User):
    rol = 'Admin'


class Gestor(User):
    rol = 'Gestor'


class Corrector(User):
    rol = 'Corrector'
