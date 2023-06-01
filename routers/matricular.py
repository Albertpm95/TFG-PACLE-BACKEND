import json
from xmlrpc.client import boolean

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud import crud
from crud import matricula as crud_matricula
from schemas.alumno import AlumnoDB
from schemas.convocatoria import ConvocatoriaDB

router = APIRouter(prefix="/matricula", tags=["Convocatoria"])

@router.post("/alumno/convocatoria", response_model=bool)
async def matricular_alumno_convocatoria(alumno: AlumnoDB, convocatoria: ConvocatoriaDB, db: Session = Depends(crud.get_db)):
    return crud_matricula.matricular_alumno_convocatoria(alumno, convocatoria, db)