from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import nivel as crud_nivel
from schemas.nivel import Nivel, NivelBase

router = APIRouter(prefix="/nivel", tags=["Nivel"])


@router.get("/list", response_model=List[Nivel])
async def recuperar_lista_niveles(db: Session = Depends(crud.get_db)):
    return crud_nivel.get_niveles(db)


@router.post("/create", response_model=Nivel)
async def create_nivel(
    nivel_nuevo: NivelBase, db: Session = Depends(crud.get_db)
) -> Nivel:
    return crud_nivel.crear_nivel(db, nivel_nuevo.nivel)


@router.delete("/delete/{idNivel}", response_model=dict[str, str])
async def delete_nivel(idNivel: int, db: Session = Depends(crud.get_db)):
    return crud_nivel.delete_nivel_id(db, idNivel)
