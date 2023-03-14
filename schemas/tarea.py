from pydantic import BaseModel


class Tarea(BaseModel):
    valor: int
    nombre_tarea: str

    class Config:
        orm_mode = True


class TareaDB(Tarea):
    id_tarea: int

    class Config:
        orm_mode = True
