from fastapi import APIRouter, UploadFile
import csv
import codecs
from constants import fake_usuarios_DB
router = APIRouter()


@router.post("/admin/upload")
async def cargar_excel(excel: UploadFile):
    numero_de_alumnos_cargados = 0
    csvReader = csv.DictReader(codecs.iterdecode(excel.file, 'utf-8'))
    data = {}
    for rows in csvReader:
        key = rows['DNI']
        data[key] = rows
    return numero_de_alumnos_cargados


@router.get("admin/usuarios")
async def recuperar_usuarios():
    return fake_usuarios_DB
