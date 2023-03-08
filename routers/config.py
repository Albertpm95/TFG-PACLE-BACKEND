from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import crud
from crud import horario as crud_horario
from crud import idioma as crud_idioma
from crud import rol as crud_rol
from models.rol_usuario import Rol
from schemas.horario import Horario
from schemas.idiomas import Idioma
from schemas.rol_usuario import Rol

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


@router.put("/config/idioma/create", response_model=Idioma)
async def create_idioma(idioma_nuevo: str, db: Session = Depends(crud.get_db)):
    return crud_idioma.crear_idioma(db=db, idioma_nuevo=idioma_nuevo)


@router.get("/config/horario/list", response_model=list[Horario])
async def recuperar_horarios_disponibles(db: Session = Depends(crud.get_db)):
    horarios = crud_horario.get_horarios(db=db)
    if not horarios:
        raise HTTPException(
            status_code=404,
            detail="No se ha podido recuperar la lista de horarios o esta vacia.",
        )
    return horarios


@router.put("/config/horario/create", response_model=Horario)
async def create_horario(horario_nuevo: str, db: Session = Depends(crud.get_db)):
    return crud_horario.crear_horario(db=db, horario_nuevo=horario_nuevo)
