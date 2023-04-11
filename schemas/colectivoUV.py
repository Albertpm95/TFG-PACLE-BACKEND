from pydantic import BaseModel


class ColectivoUVBase(BaseModel):
    colectivoUV: str

    class Config:
        orm_mode = True

class ColectivoUV(ColectivoUVBase):
    idColectivo: int

    class Config:
        orm_mode = True