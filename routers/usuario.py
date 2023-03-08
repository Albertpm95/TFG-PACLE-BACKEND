from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import usuario as crud_usuario
from crud import login as crud_login
from schemas.usuario import UsuarioBase, UsuarioCreacion, UsuarioOptional
from schemas.rol_usuario import Rol

router = APIRouter()


@router.get("/usuario/actual", response_model=UsuarioBase)
async def recuperar_usuario_actual(
    current_user: UsuarioBase = Depends(crud_login.get_current_active_user),
):
    return current_user


@router.get("/usuario/list", response_model=list[UsuarioBase])
async def recuperar_list_usuarios(db: Session = Depends(crud.get_db)):
    return crud_usuario.get_users(db)


@router.get("/usuario/{id_usuario}")
async def get_usuario_id(id_usuario: str, db: Session = Depends(crud.get_db)):
    return crud_usuario.get_user_id(db, id_usuario)


@router.get("/usuario/{username}")
async def get_usuario_username(username: str, db: Session = Depends(crud.get_db)):
    return crud_usuario.get_user_username(db, username)


@router.put("/usuario/create")
async def alta_usuario(usuario: UsuarioCreacion, db: Session = Depends(crud.get_db)):
    return crud_usuario.alta_usuario(db, usuario)


@router.patch("/usuario/disable")
async def desactivar_usuario(id_usuario: str, db: Session = Depends(crud.get_db)):
    return crud_usuario.desactivar_usuario(db, id_usuario)


@router.patch("/usuario/enable")
async def activar_usuario(id_usuario: str, db: Session = Depends(crud.get_db)):
    return crud_usuario.activar_usuario(db, id_usuario)


@router.patch("/usuario/update", response_model=UsuarioBase)
async def update_usuario(
    id_usuario, usuario_updated: UsuarioOptional, db: Session = Depends(crud.get_db)
):
    return crud_usuario.update_usuario(db, id_usuario, usuario_updated)
