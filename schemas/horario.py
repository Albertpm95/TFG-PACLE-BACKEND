from pydantic import BaseModel


class HorarioBase(BaseModel):
    horario: str

    class Config:
        orm_mode = True

class Horario(HorarioBase):
    idHorario: int

    class Config:
        orm_mode = True