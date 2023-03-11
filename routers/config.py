from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import horario as crud_horario
from crud import lenguaje as crud_idioma
from schemas.horario import Horario
from schemas.lenguaje import Lenguaje

router = APIRouter()


@router.get("/config/lenguaje/list", response_model=list[Lenguaje])
async def recuperar_idiomas_disponibles(db: Session = Depends(crud.get_db)):
    return crud_idioma.get_idiomas(db=db)


@router.put("/config/lenguaje/create", response_model=Lenguaje)
async def create_idioma(idioma_nuevo: str, db: Session = Depends(crud.get_db)):
    return crud_idioma.crear_idioma(db=db, idioma_nuevo=idioma_nuevo)


@router.get("/config/horario/list", response_model=list[Horario])
async def recuperar_horarios_disponibles(db: Session = Depends(crud.get_db)):
    return crud_horario.get_horarios(db=db)


@router.put("/config/horario/create", response_model=Horario)
async def create_horario(horario_nuevo: str, db: Session = Depends(crud.get_db)):
    return crud_horario.crear_horario(db=db, horario_nuevo=horario_nuevo)
