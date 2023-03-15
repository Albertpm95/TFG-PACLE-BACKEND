from pydantic import BaseModel


class Horario(BaseModel):
    idHorario: int
    horario: str

    class Config:
        orm_mode = True
