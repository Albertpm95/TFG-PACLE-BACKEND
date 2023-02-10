from fastapi import APIRouter
from constants import fake_actas_DB
from schemas.acta import ActaBase, IDIOMAS_DISPONIBLES, TIPOS_ACTA
from typing import get_args

router = APIRouter()


@router.get("/actas")
async def recuperar_acta(id_acta: str):
    acta = filter(lambda x: x.id_acta == id_acta, fake_actas_DB)
    return acta


@router.get("/actas/list")
async def recuperar_actas():
    actas = []
    actas = fake_actas_DB
    return actas


@router.get("/actas/idiomas")
async def recuperar_idiomas_disponibles():
    return get_args(IDIOMAS_DISPONIBLES)


@router.get("/actas/tipos")
async def recuperar_tipos_acta():
    return get_args(TIPOS_ACTA)
