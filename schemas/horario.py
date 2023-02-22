from pydantic import BaseModel


class Horario(BaseModel):
    horario: str

    class Config:
        orm_mode = True
