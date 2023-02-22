from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session

import csv
import codecs

from crud import crud
from crud import usuario as crud_usuario
from schemas.usuario import UsuarioBase, UsuarioLogin

router = APIRouter()


@router.post("/admin/upload")
async def cargar_excel(excel: UploadFile):
    numero_de_alumnos_cargados = 0
    csvReader = csv.DictReader(codecs.iterdecode(excel.file, "utf-8"))
    data = {}
    for rows in csvReader:
        key = rows["DNI"]
        data[key] = rows
    return numero_de_alumnos_cargados


@router.get("/admin/usuarios")
async def get_list_usuarios(db: Session = Depends(crud.get_db)):
    return crud_usuario.get_users(db)


@router.get("/admin/usuario/{id_usuario}")
async def get_usuario_by_id(id_usuario: str, db: Session = Depends(crud.get_db)):
    return crud_usuario.get_user_id(db, id_usuario)


@router.get("/admin/usuario/{username}")
async def get_usuario_by_username(username: str, db: Session = Depends(crud.get_db)):
    return crud_usuario.get_user_username(db, username)


@router.post("/admin/usuario/alta")
async def alta_usuario(usuario: UsuarioLogin, db: Session = Depends(crud.get_db)):
    return crud_usuario.alta_usuario(db, usuario)


@router.patch("/admin/usuario/desactivar")
async def desactivar_usuario(id_usuario: str, db: Session = Depends(crud.get_db)):
    return crud_usuario.desactivar_usuario(db, id_usuario)


@router.patch("/admin/usuario/activar")
async def activar_usuario(id_usuario: str, db: Session = Depends(crud.get_db)):
    return crud_usuario.activar_usuario(db, id_usuario)


@router.patch("/admin/usuario/update")
async def update_usuario(
    id_usuario, usuario_updated: UsuarioBase, db: Session = Depends(crud.get_db)
):
    return crud_usuario.update_usuario(db, id_usuario, usuario_updated)
