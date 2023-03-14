from pydantic import BaseModel

from constants import VALOR_PUNTUACION_MAX_DEFECTO
from schemas.tarea import Tarea


class ComprensionAuditiva(BaseModel):
    observaciones: str | None = None
    porcentaje: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntos_conseguidos: int = VALOR_PUNTUACION_MAX_DEFECTO
    puntuacion_maxima_parte: int = VALOR_PUNTUACION_MAX_DEFECTO
    tareas: list[Tarea]

    class Config:
        orm_mode = True
