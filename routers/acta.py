from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fake_db import fake_actas_corregidas_DB
from crud import crud

router = APIRouter()


@router.get("/acta/correct/{id}")
async def recuperar_acta(id: str):
    return fake_actas_corregidas_DB[0]  # TODO Change index for ID search


@router.get("/acta/list")
async def recuperar_actas():
    actas = []
    actas = fake_actas_corregidas_DB
    return actas


@router.get("/acta/idiomas")
async def recuperar_idiomas(db: Session = Depends(crud.get_db)):
    idiomas = []
    idiomas = crud.get_idiomas(db)
    return idiomas


@router.post("/acta/idiomas/{lenguaje}")
async def add_idiomas(lenguaje: str, db: Session = Depends(crud.get_db)):
    return crud.add_idiomas(db, lenguaje)
