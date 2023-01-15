from pydantic import BaseModel


class User(BaseModel):
    nombre: str
    apellido: str
    username: str


class UserDB(User):
    password: str


class Admin(User):
    rol = 'Admin'


class Gestor(User):
    rol = 'Gestor'


class Corrector(User):
    rol = 'Corrector'
