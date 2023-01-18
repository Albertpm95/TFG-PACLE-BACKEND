from fastapi import APIRouter

user = APIRouter()


@user.get("/users")
def root():
    return "Users"
