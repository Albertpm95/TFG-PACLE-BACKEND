from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import crud
from crud import convocatoria as crud_convocatoria
from schemas import convocatoria
from schemas.convocatoria import Convocatoria

router = APIRouter()


@router.get("/convocatorias/list", response_model=list[Convocatoria])
async def recuperar_lista_convocatorias(db: Session = Depends(crud.get_db)):
    convocatorias = crud_convocatoria.get_convocatorias(db)
    if not convocatorias:
        raise HTTPException(
            status_code=404,
            detail="No se ha podido recuperar la lista de convocatorias o esta vacia.",
        )
    return convocatorias


@router.get("/convocatorias/{id_convocatoria}")
async def recuperar_convocatoria_id(
    id_convocatoria: str, db: Session = Depends(crud.get_db)
):
    return crud_convocatoria.get_convocatoria_id(id_convocatoria, db)


@router.post("/convocatorias/create", response_model=convocatoria.Convocatoria)
async def crear_convocatoria(
    convocatoria: convocatoria.Convocatoria, db: Session = Depends(crud.get_db)
):
    return crud_convocatoria.create_convocatoria(convocatoria=convocatoria, db=db)


@router.get("/convocatorias/idiomas")
async def recuperar_idiomas_disponibles(db: Session = Depends(crud.get_db)):
    return crud_convocatoria.get_idiomas(db)


@router.get("/convocatorias/horarios")
async def recuperar_horarios_disponibles(db: Session = Depends(crud.get_db)):
    return crud_convocatoria.get_horarios(db)


@router.get("/convocatorias/tipos")
async def recuperar_tipos_convocatoria(db: Session = Depends(crud.get_db)):
    return crud_convocatoria.get_tipos(db)
