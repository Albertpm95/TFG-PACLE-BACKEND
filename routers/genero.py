from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import genero as crud_genero
from schemas.genero import Genero, GeneroBase

router = APIRouter(prefix="/genero", tags=["Genero"])


@router.get("/list", response_model=list[Genero])
async def recuperar_lista_generos(db: Session = Depends(crud.get_db)):
    return crud_genero.get_generos(db)


@router.post("/create", response_model=Genero)
async def create_genero(
    genero_nuevo: GeneroBase, db: Session = Depends(crud.get_db)
) -> Genero:
    return crud_genero.crear_genero(db, genero_nuevo.genero)


@router.delete("/delete/{idGenero}", response_model=dict[str, str])
async def delete_genero(
    idGenero: int, db: Session = Depends(crud.get_db)
) -> dict[str, str]:
    return crud_genero.delete_genero_id(db, idGenero)
