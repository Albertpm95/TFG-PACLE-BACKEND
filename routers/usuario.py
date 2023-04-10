from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import crud
from crud import usuario as crud_usuario
from crud import login as crud_login
from schemas.usuario import UsuarioBase, UsuarioCreacion, UsuarioDB, UsuarioLogin, UsuarioOptional

router = APIRouter(prefix="/usuario")


@router.get("/actual", response_model=UsuarioBase)
async def recuperar_usuario_actual(
    current_user: UsuarioBase = Depends(crud_login.get_current_active_user),
) -> UsuarioBase:
    return current_user


@router.get("/list", response_model=list[UsuarioDB])
async def recuperar_list_usuarios(db: Session = Depends(crud.get_db)) -> list[UsuarioDB]:
    return crud_usuario.get_users(db)


@router.get("/details/{id_usuario}", response_model=UsuarioBase)
async def get_usuario_id(id_usuario: str, db: Session = Depends(crud.get_db)) -> UsuarioDB:
    return crud_usuario.get_user_id(db, id_usuario)


@router.get("/details/{username}", response_model=UsuarioBase)
async def get_usuario_username(username: str, db: Session = Depends(crud.get_db)) -> UsuarioDB:
    return crud_usuario.get_user_username(db, username)


@router.put("/create", response_model=UsuarioBase)
async def create_usuario(usuario: UsuarioCreacion, db: Session = Depends(crud.get_db)) -> UsuarioDB:
    return crud_usuario.create_usuario(db, usuario)


@router.patch("/disable", response_model=UsuarioBase)
async def desactivar_usuario(id_usuario: str, db: Session = Depends(crud.get_db)) -> UsuarioDB:
    return crud_usuario.desactivar_usuario(db, id_usuario)


@router.patch("/enable", response_model=UsuarioBase)
async def activar_usuario(id_usuario: str, db: Session = Depends(crud.get_db)) -> UsuarioDB:
    return crud_usuario.activar_usuario(db, id_usuario)


@router.patch("/update", response_model=UsuarioBase)
async def update_usuario(
    id_usuario, usuario_updated: UsuarioOptional, db: Session = Depends(crud.get_db)
) -> UsuarioDB:
    return crud_usuario.update_usuario(db, id_usuario, usuario_updated)
