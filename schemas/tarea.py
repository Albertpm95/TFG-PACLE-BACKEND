from pydantic import BaseModel

class Tarea(BaseModel):
  alcance: int
  coherencia: int
  correccion: int
  eficaciaC: int
  id_corrector: str | None = None
  nombre_corrector: str | None = None