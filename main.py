from fastapi import FastAPI, Depends, status
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

import environment
import models.shared as shared
from schemas import Usuario, UsuarioLogin

app = FastAPI()

manager = LoginManager(environment.SECRET, "/login")
origins = ["http://localhost:4200",
           "http://localhost:4200/", "http://localhost:4200/*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_DB = [
    {
        "name": "Rick",
        "lastname": "Sanchez",
        "password": "1234",
        "username": "rick_sanchez",
        "rol": "gestor",
    },
    {
        "name": "Morty",
        "lastname": "Smith",
        "password": "1234",
        "username": "morty_smith",
        "rol": "corrector",
    },
    {
        "name": "Jerry",
        "lastname": "Smith",
        "password": "1234",
        "username": "jerry_smith",
        "rol": "administrador",
    },
]


@app.get("/")
async def root():
    return {"message": "Root"}


# Tests


@app.get("/get_plural/")
async def get_plural():
    return fake_DB


@app.get("/get_1/{acta_id}")
async def get_1(acta_id):
    return {"Get ": acta_id}


@app.get("/get_2/{acta_id}")
async def get_2(acta_id: int):
    return {"Int acta_id": acta_id}


@app.post("/post_1")
async def post_1(username: str):
    return {'message', 'Hola ' + username}


@app.post("/post_2")
async def post_2(username: str, password: str):
    return {'message', 'Hola ', username, ' tu contraseña es ', password}


@app.post("/post_3")
async def post_3(usuario: Usuario):
    return {'message', 'Hola Usuario: ', ' tu username es: ', usuario.username, ' y tu contraseña es ', usuario.password}
