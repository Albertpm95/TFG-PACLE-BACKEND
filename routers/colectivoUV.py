from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from crud import colectivoUV as crud_colectivoUV
from crud import crud
from schemas.colectivoUV import ColectivoUV, ColectivoUVBase

router = APIRouter(prefix="/colectivoUV", tags=["Colectivo UV"])


@router.get("/list", response_model=List[ColectivoUV])
async def recuperar_lista_colectivosUV(
    db: Session = Depends(crud.get_db),
):
    return crud_colectivoUV.get_colectivosUV(db)


@router.post("/create", response_model=ColectivoUV)
async def create_colectivo(
    colectivoUV_nuevo: ColectivoUVBase, db: Session = Depends(crud.get_db)
) -> ColectivoUV:

    return crud_colectivoUV.crear_colectivoUV(
        db, colectivoUV_nuevo=colectivoUV_nuevo.colectivoUV
    )


@router.delete("/delete/{idColectivoUV}", response_model=dict[str, str])
async def delete_colectivoUV(idColectivoUV: int, db: Session = Depends(crud.get_db)):
    return crud_colectivoUV.delete_colectivoUV_id(db, idColectivoUV)
