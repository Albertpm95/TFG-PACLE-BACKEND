from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from environment import ACCESS_TOKEN_EXPIRE_MINUTES

from crud import crud
from crud import login as crud_login
from schemas.token import Token

router = APIRouter()


@router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(crud.get_db)
):
    usuario = crud_login.authenticate_user(form_data.username, form_data.password, db)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud_login.create_access_token(
        data={"sub": usuario.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
