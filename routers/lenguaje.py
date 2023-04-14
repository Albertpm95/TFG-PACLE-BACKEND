from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import lenguaje as crud_idioma
from schemas.lenguaje import Lenguaje, LenguajeBase

router = APIRouter(prefix="/config", tags=["Config"])


@router.get("/list", response_model=list[Lenguaje])
async def recuperar_lista_idiomas(db: Session = Depends(crud.get_db)):
    return crud_idioma.get_idiomas(db)


@router.post("/create", response_model=Lenguaje)
async def create_lenguaje(
    lenguaje_nuevo: LenguajeBase, db: Session = Depends(crud.get_db)
) -> Lenguaje:
    return crud_idioma.crear_lenguaje(db, lenguaje_nuevo.lenguaje)


@router.delete("/delete/{idLenguaje}", response_model=dict[str, str])
async def delete_lenguaje(
    idLenguaje: int, db: Session = Depends(crud.get_db)
) -> dict[str, str]:
    return crud_idioma.delete_idioma_id(db, idLenguaje)
