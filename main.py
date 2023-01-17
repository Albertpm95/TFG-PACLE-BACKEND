from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from db.models.user import UserDB, User


app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


@app.get("/")
async def hello():
    return 'Connection established'
