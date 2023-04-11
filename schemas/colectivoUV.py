from pydantic import BaseModel


class ColectivoUVBase(BaseModel):
    colectivo: str

    class Config:
        orm_mode = True

class ColectivoUV(ColectivoUVBase):
    idColectivo: int

    class Config:
        orm_mode = True