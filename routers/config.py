from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud
from schemas.horario import Horario

from schemas.idiomas import Idioma


from crud import horario as crud_horario
from crud import idioma as crud_idioma

router = APIRouter()


@router.get("/config/idioma/list", response_model=list[Idioma])
async def recuperar_idiomas_disponibles(db: Session = Depends(crud.get_db)):
    idiomas = crud_idioma.get_idiomas(db=db)
    if not idiomas:
        raise HTTPException(
            status_code=404,
            detail="No se ha podido recuperar la lista de idiomas o esta vacia.",
        )
    return idiomas


@router.get("/config/horario/list", response_model=list[Horario])
async def recuperar_horarios_disponibles(db: Session = Depends(crud.get_db)):
    horarios = crud_horario.get_horarios(db=db)
    if not horarios:
        raise HTTPException(
            status_code=404,
            detail="No se ha podido recuperar la lista de horarios o esta vacia.",
        )
    return horarios
