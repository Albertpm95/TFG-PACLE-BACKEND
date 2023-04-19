from pydantic import BaseModel

from schemas.usuario import UsuarioBase


class Tarea(BaseModel):
    nombreTarea: str

    class Config:
        orm_mode = True


class TareaDB(Tarea):
    idTarea: int

    class Config:
        orm_mode = True
        
class TareaCorregida(TareaDB):
    puntuacion: int

    class Config:   
        orm_mode = True

class TareaCorregidaDB(TareaCorregida):
    idTareaCorregida: int