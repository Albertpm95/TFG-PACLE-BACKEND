from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    id: int
    nombre: str
    apellido: str
    usuario: str
    password: str


class UserDB(User):
    password: str


class Admin(User):
    rol = 'Admin'


class Gestor(User):
    rol = 'Gestor'


class Corrector(User):
    rol = 'Corrector'


users_db = {
    "rick": {
        "nombre": "Rick",
        "apellido": "Sanchez",
        "usuario": "rick_sanchez",
        "password": "123456",
    },
    "morty": {
        "nombre": "Morty",
        "apellido": "Smith",
        "usuario": "rick_sanchez",
        "password": "123456",
    },
    "jerry": {
        "nombre": "Jerry",
        "apellido": "Smith",
        "usuario": "rick_sanchez",
        "password": "123456",
    },
}


def search_user(usuario: str):
    if usuario in users_db:
        return UserDB(users_db[usuario])


async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autentificación invalidas.",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_dab = users_db.get(form.username)
    if not users_db:
        raise HTTPException(
            status_code=400, detail="El usuario no existe."
        )
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=400, detail="El usuario o la contraseña no son correctos."
        )
    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
