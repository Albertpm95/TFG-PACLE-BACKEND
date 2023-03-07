from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import crud
from crud import convocatoria as crud_convocatoria

from schemas import convocatoria
from schemas.convocatoria import Convocatoria

router = APIRouter()


@router.get("/convocatoria/list", response_model=list[Convocatoria])
async def recuperar_lista_convocatorias(db: Session = Depends(crud.get_db)):
    convocatorias = crud_convocatoria.get_convocatorias(db)
    if not convocatorias:
        raise HTTPException(
            status_code=404,
            detail="No se ha podido recuperar la lista de convocatorias o esta vacia.",
        )
    return convocatorias


@router.get("/convocatoria/{id_convocatoria}")
async def recuperar_convocatoria_id(
    id_convocatoria: str, db: Session = Depends(crud.get_db)
):
    return crud_convocatoria.get_convocatoria_id(id_convocatoria, db)


@router.put("/convocatoria/create", response_model=convocatoria.Convocatoria)
async def crear_convocatoria(
    convocatoria: convocatoria.Convocatoria, db: Session = Depends(crud.get_db)
):
    return crud_convocatoria.create_convocatoria(convocatoria=convocatoria, db=db)
