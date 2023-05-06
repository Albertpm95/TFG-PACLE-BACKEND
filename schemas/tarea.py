from pydantic import BaseModel


class Tarea(BaseModel):
    nombreTarea: str

    class Config:
        orm_mode = True


class TareaDB(Tarea):
    idTarea: int
    idParte: int

    class Config:
        orm_mode = True
        
class TareaCorregida(TareaDB):
    puntuacion: int

    class Config:   
        orm_mode = True

class TareaCorregidaDB(TareaCorregida):
    idTareaCorregida: int