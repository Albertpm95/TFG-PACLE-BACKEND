from fastapi import APIRouter
from fake_db import fake_actas_corregidas_DB

router = APIRouter()


@router.get("/acta/correct/{id}")
async def recuperar_acta(id: str): 
    return fake_actas_corregidas_DB[0]  # TODO Change index for ID search


@router.get("/acta/list")
async def recuperar_actas():
    actas = []
    actas = fake_actas_corregidas_DB
    return actas
