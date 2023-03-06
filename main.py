from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from routers import convocatoria, login, usuario, alumno, acta, admin, config

app = FastAPI()

app.include_router(login.router)
app.include_router(convocatoria.router)
app.include_router(usuario.router)
app.include_router(alumno.router)
app.include_router(admin.router)
app.include_router(acta.router)
app.include_router(config.router)

origins = ["http://localhost:4200*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    raise HTTPException(status_code=200, detail="Hay conexion con el servidor.")
