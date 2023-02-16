from fastapi import APIRouter
from typing import get_args
from constants import HORARIOS, IDIOMAS_DISPONIBLES, TIPOS_ACTA
from fake_db import fake_convocatorias_nuevas_DB

router = APIRouter()


@router.get("/acta/correct/{id}")
async def recuperar_acta(id: str):
    return fake_convocatorias_nuevas_DB[1]


@router.get("/acta/list")
async def recuperar_actas():
    actas = []
    actas = fake_convocatorias_nuevas_DB
    return actas


@router.get("/acta/idiomas")
async def recuperar_idiomas_disponibles():
    return get_args(IDIOMAS_DISPONIBLES)

@router.get("/acta/horarios")
async def recuperar_horarios_disponibles():
    return get_args(HORARIOS)

@router.get("/acta/tipos")
async def recuperar_tipos_acta():
    return get_args(TIPOS_ACTA)


@router.get("/acta/tipos")
async def recuperar_horarios_acta():
    return get_args(TIPOS_ACTA)
