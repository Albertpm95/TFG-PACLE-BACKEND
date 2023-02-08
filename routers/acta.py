from fastapi import APIRouter
from constants import fake_actas_DB
from schemas.acta import Acta
router = APIRouter()


@router.get("/actas")
async def recuperar_actas():
    actas = []
    actas = fake_actas_DB
    return actas


@router.get("/actas")
async def recuperar_acta(acta_id: str):
    acta = filter(lambda x: x.acta_id == acta_id, fake_actas_DB)
    return acta
