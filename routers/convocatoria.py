from fastapi import APIRouter
from typing import get_args
from constants import HORARIOS, IDIOMAS_DISPONIBLES, TIPOS_ACTA
from fake_db import fake_convocatorias_nuevas_DB

router = APIRouter()


@router.get("/convocatorias/{id}")
async def recuperar_convocatoria(id: str):
    return fake_convocatorias_nuevas_DB[0]  # TODO Change index for id


@router.get("/convocatorias")
async def recuperar_convocatorias():
    return fake_convocatorias_nuevas_DB


@router.get("/convocatoria/idiomas")
async def recuperar_idiomas_disponibles():
    return get_args(IDIOMAS_DISPONIBLES)


@router.get("/convocatoria/horarios")
async def recuperar_horarios_disponibles():
    return get_args(HORARIOS)


@router.get("/convocatoria/tipos")
async def recuperar_tipos_acta():
    return get_args(TIPOS_ACTA)
