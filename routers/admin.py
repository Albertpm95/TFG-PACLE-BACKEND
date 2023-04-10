import codecs
import csv

from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session

from crud import crud


router = APIRouter(prefix="/admin")


@router.post("/upload", response_model=int)
async def cargar_excel(excel: UploadFile, db: Session = Depends(crud.get_db)):
    numero_de_alumnos_cargados = 0
    csvReader = csv.DictReader(codecs.iterdecode(excel.file, "utf-8"))
    data = {}
    for rows in csvReader:
        key = rows["DNI"]
        data[key] = rows
    return numero_de_alumnos_cargados
