from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import crud
from crud import convocatoria as crud_convocatoria

from schemas.convocatoria import Convocatoria, ConvocatoriaDB

router = APIRouter()


@router.get("/convocatoria/list", response_model=list[ConvocatoriaDB])
async def recuperar_lista_convocatorias(db: Session = Depends(crud.get_db)):
    return crud_convocatoria.get_convocatorias(db)


@router.get("/convocatoria/update/{id_convocatoria}", response_model=ConvocatoriaDB)
async def recuperar_convocatoria_id(
    id_convocatoria: int, db: Session = Depends(crud.get_db)
):
    return crud_convocatoria.get_convocatoria_id(id_convocatoria=id_convocatoria, db=db)


@router.put("/convocatoria/create", response_model=ConvocatoriaDB)
async def create_convocatoria(
    convocatoria: Convocatoria, db: Session = Depends(crud.get_db)
):
    return crud_convocatoria.create_convocatoria(convocatoria=convocatoria, db=db)


@router.post("/convocatoria/update", response_model=ConvocatoriaDB)
async def update_convocatoria(
    convocatoria: ConvocatoriaDB, db: Session = Depends(crud.get_db)
):
    return crud_convocatoria.update_convocatoria(convocatoria=convocatoria, db=db)
