from fastapi import APIRouter, File, UploadFile
import csv
import codecs
from constants import lista_acciones
router = APIRouter()


@router.post("/admin/upload")
async def upload_excel(excel: UploadFile):
    numero_de_alumnos_cargados = 0
    csvReader = csv.DictReader(codecs.iterdecode(excel.file, 'utf-8'))
    data = {}
    for rows in csvReader:
        key = rows['DNI']
        data[key] = rows
    return numero_de_alumnos_cargados
