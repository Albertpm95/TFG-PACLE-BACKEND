from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session


from crud import crud
from crud import acta as crud_acta

router = APIRouter()


@router.get("/acta/correct/{id}")
async def recuperar_acta(id_acta: str, db: Session = Depends(crud.get_db)):
    return crud_acta.get_convocatoria_id(id_acta, db)


@router.get("/acta/list")
async def recuperar_actas(db: Session = Depends(crud.get_db)):
    return crud_acta.get_convocatorias(db)
