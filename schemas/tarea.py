from pydantic import BaseModel

from schemas.usuario import UsuarioBase


class Tarea(BaseModel):
    valor: int
    nombre_tarea: str

    class Config:
        orm_mode = True


class TareaDB(Tarea):
    id_tarea: int

    class Config:
        orm_mode = True
        
class TareaCorregida(TareaDB):
    puntuacion: int

    class Config:   
        orm_mode = True

class TareaCorregidaDB(TareaCorregida):
    idTareaCorregida: int