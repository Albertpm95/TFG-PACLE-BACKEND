from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from crud import crud
from crud import usuario as crud_usuario
from schemas.usuario import UsuarioLogin

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def fake_hash_password(password: str):
    return "fakehashed" + password


def fake_decode_token(token, db: Session = Depends(crud.get_db)):
    user = crud_usuario.get_user_username(db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autentificacion invalidas.",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(crud.get_db)
):
    user_dict = crud_usuario.get_user_username(db, form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos.")
    usuario_sch = UsuarioLogin(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == usuario_sch.hashed_password:
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos.")

    return {"access_token": usuario_sch.username, "token_type": "bearer"}
