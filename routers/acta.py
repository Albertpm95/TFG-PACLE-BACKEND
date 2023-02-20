from fastapi import APIRouter, Depends, Query
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
async def add_idioma(lenguaje: str, db: Session = Depends(crud.get_db)):
    return crud.add_idioma(db, lenguaje)


@router.get("/acta/tipos")
async def recuperar_tipos(db: Session = Depends(crud.get_db)):
    idiomas = []
    idiomas = crud.get_tipos(db)
    return idiomas


@router.post("/acta/tipos/{tipo}")
async def add_tipo(tipo: str, db: Session = Depends(crud.get_db)):
    return crud.add_tipo(db, tipo)


@router.get("/acta/horarios")
async def recuperar_horarios(db: Session = Depends(crud.get_db)):
    idiomas = []
    idiomas = crud.get_horarios(db)
    return idiomas


@router.post("/acta/horarios/{horario}")
async def add_horario(
    horario: str = Query(regex="/^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/"),
    db: Session = Depends(crud.get_db),
):
    return crud.add_horario(db, horario)
