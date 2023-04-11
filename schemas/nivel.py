from pydantic import BaseModel


class NivelBase(BaseModel):
    nivel: str

    class Config:
        orm_mode = True


class Nivel(NivelBase):
    idNivel: int

    class Config:
        orm_mode = True
