from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import convocatoria as convocatoria_crud

router = APIRouter()


@router.get("/convocatorias/{id_convocatoria}")
async def recuperar_convocatoria_id(
    id_convocatoria: str, db: Session = Depends(crud.get_db)
):
    return convocatoria_crud.get_convocatoria_id(id_convocatoria, db)


@router.get("/convocatorias")
async def recuperar_convocatorias(db: Session = Depends(crud.get_db)):
    return convocatoria_crud.get_convocatorias(db)


@router.get("/convocatoria/idiomas")
async def recuperar_idiomas_disponibles(db: Session = Depends(crud.get_db)):
    return convocatoria_crud.get_idiomas(db)


@router.get("/convocatoria/horarios")
async def recuperar_horarios_disponibles(db: Session = Depends(crud.get_db)):
    return convocatoria_crud.get_horarios(db)


@router.get("/convocatoria/tipos")
async def recuperar_tipos_acta(db: Session = Depends(crud.get_db)):
    return convocatoria_crud.get_tipos(db)
