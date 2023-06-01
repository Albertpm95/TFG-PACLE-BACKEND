from pydantic import BaseModel


class Tarea(BaseModel):
    nombreTarea: str

    class Config:
        orm_mode = True
