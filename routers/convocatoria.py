from datetime import date, time
from fastapi import APIRouter

router = APIRouter()


class ComprensionLectora():
    peso_parte: int
    observaciones: str
    tarea_1: int
    tarea_2: int
    tarea_3: int


class ComprensionAuditiva():
    peso_parte: int
    observaciones: str
    tarea_1: int
    tarea_2: int
    tarea_3: int


class ExpresionEscrita():
    peso_parte: int
    observaciones: str
    tarea_1: int  # Eficacia C., Coherencia, Alcance, Correccion
    tarea_2: int  # Eficacia C., Coherencia, Alcance, Correccion


class ExpresionOral():
    peso_parte: int
    observaciones: str
    tarea_1: int  # Eficacia C., Coherencia, Alcance, Correccion
    tarea_2: int  # Eficacia C., Coherencia, Alcance, Correccion


class Convocatoria():
    id: int
    tipo: str  # Ordinaria | Extraordinaria
    fecha: date
    hora: time
    resultado_lectura_escritura: int
    resultado_destrezas_orales: int
    resultado_global: int
    calificacion: int
