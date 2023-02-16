from pydantic import BaseModel
from schemas.tarea import Tarea


class Expresion(BaseModel):
  observaciones: str | None = None
  pocentaje: int
  puntosConseguidos: int
  puntuacionMaximaParte: int
  tarea1: Tarea
  tarea2: Tarea