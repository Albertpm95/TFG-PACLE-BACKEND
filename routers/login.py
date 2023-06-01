import os
from datetime import timedelta
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from crud import crud
from crud import login as crud_login
from schemas.token import Token
from schemas.usuario import UsuarioLogin

ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

router = APIRouter(prefix="/login", tags=["Login"])

@router.post("", response_model=Token)
async def login_for_access_token(
    formData: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(crud.get_db)
) -> dict[str, str]:
    usuario: UsuarioLogin | Literal[False] = crud_login.authenticate_user(
        formData.username, formData.password, db
    )
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token: str = crud_login.create_access_token(
        data={"sub": usuario.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
