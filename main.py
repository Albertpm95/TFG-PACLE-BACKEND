from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

load_dotenv("environment.env")

import db.database  # noqa: E402

# noqa: E402
from routers import login  # noqa: E402
from routers import acta, admin, alumno, config, convocatoria, matricular, usuario

app = FastAPI(title="TFG-Pacle-API", debug=True)

app.include_router(login.router)
app.include_router(convocatoria.router)
app.include_router(usuario.router)
app.include_router(alumno.router)
app.include_router(admin.router)
app.include_router(acta.router)
app.include_router(config.router)
app.include_router(matricular.router)

origins = ["*"]

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


def main():
    db.database.create_db_and_tables()
    db.database.create_roles()
