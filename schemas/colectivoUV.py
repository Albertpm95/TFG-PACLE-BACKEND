from pydantic import BaseModel


class ColectivoUV(BaseModel):
    idColectivo: int
    colectivo: str

    class Config:
        orm_mode = True
