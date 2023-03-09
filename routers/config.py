from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import horario as crud_horario
from crud import idioma as crud_idioma
from schemas.horario import Horario
from schemas.idiomas import Idioma

router = APIRouter()


@router.get("/config/idioma/list", response_model=list[Idioma])
async def recuperar_idiomas_disponibles(db: Session = Depends(crud.get_db)):
    return crud_idioma.get_idiomas(db=db)


@router.put("/config/idioma/create", response_model=Idioma)
async def create_idioma(idioma_nuevo: str, db: Session = Depends(crud.get_db)):
    return crud_idioma.crear_idioma(db=db, idioma_nuevo=idioma_nuevo)


@router.get("/config/horario/list", response_model=list[Horario])
async def recuperar_horarios_disponibles(db: Session = Depends(crud.get_db)):
    return crud_horario.get_horarios(db=db)


@router.put("/config/horario/create", response_model=Horario)
async def create_horario(horario_nuevo: str, db: Session = Depends(crud.get_db)):
    return crud_horario.crear_horario(db=db, horario_nuevo=horario_nuevo)
