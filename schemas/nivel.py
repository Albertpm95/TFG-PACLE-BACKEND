from pydantic import BaseModel


class Nivel(BaseModel):
    idNivel: int
    nivel: str

    class Config:
        orm_mode = True
