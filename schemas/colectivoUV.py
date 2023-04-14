from pydantic import BaseModel


class ColectivoUVBase(BaseModel):
    colectivoUV: str

    class Config:
        orm_mode = True


class ColectivoUV(ColectivoUVBase):
    idColectivoUV: int

    class Config:
        orm_mode = True
