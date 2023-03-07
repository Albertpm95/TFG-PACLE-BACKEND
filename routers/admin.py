from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session

import csv
import codecs

from crud import crud
from crud import usuario as crud_usuario
from crud import rol as crud_rol
from crud import tipo as crud_tipo
from crud import horario as crud_horario
from crud import idioma as crud_idioma
from schemas.usuario import UsuarioBase, UsuarioCreacion, UsuarioLogin, UsuarioOptional
from schemas.rol_usuario import Rol
from schemas.idiomas import Idioma
from schemas.tipo import Tipo
from schemas.horario import Horario

router = APIRouter()


@router.get("/admin/usuario/list", response_model=list[UsuarioBase])
async def recuperar_list_usuarios(db: Session = Depends(crud.get_db)):
    return crud_usuario.get_users(db)


@router.post("/admin/upload")
async def cargar_excel(excel: UploadFile):
    numero_de_alumnos_cargados = 0
    csvReader = csv.DictReader(codecs.iterdecode(excel.file, "utf-8"))
    data = {}
    for rows in csvReader:
        key = rows["DNI"]
        data[key] = rows
    return numero_de_alumnos_cargados


@router.get("/admin/usuario/{id_usuario}")
async def get_usuario_id(id_usuario: str, db: Session = Depends(crud.get_db)):
    return crud_usuario.get_user_id(db, id_usuario)


@router.get("/admin/usuario/{username}")
async def get_usuario_username(username: str, db: Session = Depends(crud.get_db)):
    return crud_usuario.get_user_username(db, username)


@router.put("/admin/usuario/create")
async def alta_usuario(usuario: UsuarioCreacion, db: Session = Depends(crud.get_db)):
    return crud_usuario.alta_usuario(db, usuario)


@router.patch("/admin/usuario/disable")
async def desactivar_usuario(id_usuario: str, db: Session = Depends(crud.get_db)):
    return crud_usuario.desactivar_usuario(db, id_usuario)


@router.patch("/admin/usuario/enable")
async def activar_usuario(id_usuario: str, db: Session = Depends(crud.get_db)):
    return crud_usuario.activar_usuario(db, id_usuario)


@router.patch("/admin/usuario/update", response_model=UsuarioBase)
async def update_usuario(
    id_usuario, usuario_updated: UsuarioOptional, db: Session = Depends(crud.get_db)
):
    return crud_usuario.update_usuario(db, id_usuario, usuario_updated)


@router.put("/admin/rol/create", response_model=Rol)
async def create_rol(rol: str, db: Session = Depends(crud.get_db)):
    return crud_rol.crear_rol(db=db, rol_nuevo=rol)


@router.put("/admin/horario/create", response_model=Horario)
async def create_horario(horario_nuevo: str, db: Session = Depends(crud.get_db)):
    return crud_horario.crear_horario(db=db, horario_nuevo=horario_nuevo)


@router.put("/admin/tipo/create", response_model=Tipo)
async def create_tipo(tipo: str, db: Session = Depends(crud.get_db)):
    return crud_tipo.crear_tipo(db=db, tipo_nuevo=tipo)


@router.put("/admin/idioma/create", response_model=Idioma)
async def create_idioma(idioma_nuevo: str, db: Session = Depends(crud.get_db)):
    return crud_idioma.crear_idioma(db=db, idioma_nuevo=idioma_nuevo)
