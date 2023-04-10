from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import horario as crud_horario
from crud import lenguaje as crud_idioma
from crud import nivel as crud_nivel
from schemas.horario import Horario
from schemas.lenguaje import Lenguaje
from schemas.nivel import Nivel

router = APIRouter(prefix="/config")


@router.get("/lenguaje/list", response_model=list[Lenguaje])
async def recuperar_idiomas_disponibles(db: Session = Depends(crud.get_db)):
    return crud_idioma.get_idiomas(db=db)


@router.put("/lenguaje/create", response_model=Lenguaje)
async def create_idioma(idioma_nuevo: str, db: Session = Depends(crud.get_db)):
    return crud_idioma.crear_idioma(db=db, idioma_nuevo=idioma_nuevo)


@router.get("/horario/list", response_model=list[Horario])
async def recuperar_horarios_disponibles(db: Session = Depends(crud.get_db)):
    return crud_horario.get_horarios(db=db)


@router.put("/horario/create", response_model=Horario)
async def create_horario(horario_nuevo: str, db: Session = Depends(crud.get_db)):
    return crud_horario.crear_horario(db=db, horario_nuevo=horario_nuevo)


@router.get("/nivel/list", response_model=list[Nivel])
async def recuperar_niveles_disponibles(db: Session = Depends(crud.get_db)):
    return crud_nivel.get_niveles(db=db)


@router.put("/nivel/create", response_model=Nivel)
async def create_nivel(nivel_nuevo: str, db: Session = Depends(crud.get_db)):
    return crud_nivel.crear_nivel(db=db, nivel_nuevo=nivel_nuevo)
