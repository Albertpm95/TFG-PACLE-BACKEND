from pydantic import BaseModel


class Horario(BaseModel):
    id_horario: int
    horario: str

    class Config:
        orm_mode = True
