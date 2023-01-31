from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_login import LoginManager

app = FastAPI()

origins = ["http://localhost:4200", "http://localhost:4200/", "http://localhost:4200/*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Root"}


@app.post("/login")
async def test_2():
    return {"message": "Test 2"}


@app.get("/test_2")
async def test_2():
    return {"message": "Test 2"}


@app.get("/test_3")
async def test_3():
    return {"message": "Test 3"}
