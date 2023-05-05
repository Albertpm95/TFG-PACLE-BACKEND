import json

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud import convocatoria as crud_convocatoria
from crud import crud
from schemas.convocatoria import ConvocatoriaDB, ConvocatoriaNueva

router = APIRouter(prefix="/convocatoria", tags=["Convocatoria"])


@router.get("/list", response_model=list[ConvocatoriaDB])
async def recuperar_lista_convocatorias(
    db: Session = Depends(crud.get_db),
) -> list[ConvocatoriaDB]:
    return crud_convocatoria.get_convocatorias(db)


@router.get("/details/{idConvocatoria}", response_model=ConvocatoriaDB)
async def recuperar_convocatoria_id(
    idConvocatoria: int, db: Session = Depends(crud.get_db)
) -> ConvocatoriaDB:
    return crud_convocatoria.get_convocatoria_id(idConvocatoria=idConvocatoria, db=db)


@router.post("/create", response_model=ConvocatoriaDB)
async def create_convocatoria(
    convocatoria_nueva: ConvocatoriaNueva, db: Session = Depends(crud.get_db)
):
    return crud_convocatoria.create_convocatoria(convocatoria=convocatoria_nueva, db=db)


@router.put("/update", response_model=ConvocatoriaDB)
async def update_convocatoria(
    convocatoria_update: ConvocatoriaDB, db: Session = Depends(crud.get_db)
) -> ConvocatoriaDB:
    print(  )
    print(json.dumps(jsonable_encoder(convocatoria_update), indent=4))
    print(  )
    return crud_convocatoria.update_convocatoria(convocatoria_update=convocatoria_update, db=db)
