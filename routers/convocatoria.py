from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import crud
from crud import convocatoria as crud_convocatoria

from schemas.convocatoria import Convocatoria, ConvocatoriaDB

router = APIRouter(prefix="/convocatoria", tags=["Convocatoria"])


@router.get("/list", response_model=list[ConvocatoriaDB])
async def recuperar_lista_convocatorias(
    db: Session = Depends(crud.get_db),
) -> list[ConvocatoriaDB]:
    return crud_convocatoria.get_convocatorias(db)


@router.get("/details/{idConvocatoria}", response_model=ConvocatoriaDB)
async def recuperar_convocatoria_id(
    idConvocatoria: int, db: Session = Depends(crud.get_db)
) -> ConvocatoriaDB:
    return crud_convocatoria.get_convocatoria_id(idConvocatoria=idConvocatoria, db=db)


@router.post("/create", response_model=ConvocatoriaDB)
async def create_convocatoria(
    convocatoria: Convocatoria, db: Session = Depends(crud.get_db)
) -> ConvocatoriaDB:
    return crud_convocatoria.create_convocatoria(convocatoria=convocatoria, db=db)


@router.put("/update", response_model=ConvocatoriaDB)
async def update_convocatoria(
    convocatoria: ConvocatoriaDB, db: Session = Depends(crud.get_db)
) -> ConvocatoriaDB:
    return crud_convocatoria.update_convocatoria(convocatoria=convocatoria, db=db)
