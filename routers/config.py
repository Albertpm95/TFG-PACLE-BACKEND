from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import horario as crud_horario
from crud import lenguaje as crud_idioma
from crud import nivel as crud_nivel
from crud import colectivoUV as crud_colectivoUV
from crud import genero as crud_genero

from schemas.colectivoUV import ColectivoUV
from schemas.horario import Horario
from schemas.lenguaje import Lenguaje
from schemas.nivel import Nivel
from schemas.genero import Genero

router = APIRouter(prefix="/config")


@router.get("/lenguaje/list", response_model=list[Lenguaje])
async def recuperar_lista_idiomas(db: Session = Depends(crud.get_db)):
    return crud_idioma.get_idiomas(db)


@router.put("/lenguaje/create", response_model=Lenguaje)
async def create_lenguaje(
    lenguaje_nuevo: str, db: Session = Depends(crud.get_db)
) -> Lenguaje | None:
    return crud_idioma.crear_lenguaje(db, lenguaje_nuevo)


@router.get("/horario/list", response_model=list[Horario])
async def recuperar_lista_horarios(db: Session = Depends(crud.get_db)):
    return crud_horario.get_horarios(db)


@router.put("/horario/create", response_model=Horario)
async def create_horario(
    horario_nuevo: str, db: Session = Depends(crud.get_db)
) -> Horario:
    return crud_horario.crear_horario(db, horario_nuevo)


@router.get("/nivel/list", response_model=list[Nivel])
async def recuperar_lista_niveles(db: Session = Depends(crud.get_db)):
    return crud_nivel.get_niveles(db)


@router.put("/nivel/create", response_model=Nivel)
async def create_nivel(nivel_nuevo: str, db: Session = Depends(crud.get_db)) -> Nivel:
    return crud_nivel.crear_nivel(db, nivel_nuevo)


@router.get("/colectivoUV/list", response_model=list[ColectivoUV])
async def recuperar_lista_colectivosUV(
    db: Session = Depends(crud.get_db),
):
    return crud_colectivoUV.get_colectivosUV(db)


@router.put("/colectivoUV/create", response_model=ColectivoUV)
async def create_colectivo(
    colectivoUV_nuevo: str, db: Session = Depends(crud.get_db)
) -> ColectivoUV:
    return crud_colectivoUV.crear_colectivoUV(db, colectivoUV_nuevo)


@router.get("/genero/list", response_model=list[Genero])
async def recuperar_lista_generos(db: Session = Depends(crud.get_db)):
    return crud_genero.get_generos(db)


@router.put("/genero/create", response_model=Genero)
async def create_genero(
    genero_nuevo: str, db: Session = Depends(crud.get_db)
) -> Genero:
    return crud_genero.crear_genero(db, genero_nuevo)
