from datetime import datetime, timedelta
from typing import Any, Literal

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from crud import crud
from crud import usuario as crud_usuario
from models.usuario import Usuario
from schemas.token import TokenData
from schemas.usuario import UsuarioBase, UsuarioDB, UsuarioLogin

from jose import JWTError, jwt

import os

ALGORITHM: str | None = os.getenv("ALGORITHM")
SECRET_KEY: str | None = os.getenv("SECRET_KEY")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(
    username: str, password: str, db: Session
) -> UsuarioLogin | Literal[False]:
    usuario: Usuario = crud_usuario.get_user_username(db, username)
    if not usuario:
        raise HTTPException(status_code=400, detail="El usuario no existe.")
    if not crud.verify_password(
        plain_password=password, usuario_db_hashed_password=usuario.hashedPassword
    ):
        return HTTPException(status_code=403, details="Unauthorized")
    return usuario


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode: dict = data.copy()
    if expires_delta:
        expire: datetime = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt: str = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UsuarioDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se han podido validar las credenciales.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload: dict[str, Any] = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: Any | None = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    db: Session = Depends(crud.get_db)
    usuario: Usuario = crud_usuario.get_user_username(db, token_data.username)
    if usuario is None:
        raise credentials_exception
    return usuario


async def get_current_active_user(
    current_user: UsuarioBase = Depends(get_current_user),
):
    if current_user.estado:
        raise HTTPException(status_code=400, detail="Usuario desactivado")
    return current_user
