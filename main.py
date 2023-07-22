from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("574ef5ae-41ed-4988-a3e4-1502b53143fc"),
        first_name="Irakli",
        last_name="Khonelidze",
        middle_name="",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("119eecea-d0f2-4b4e-9518-3f707fc16968"),
        first_name="Irakli",
        last_name="Khonelidze",
        middle_name="",
        gender=Gender.female,
        roles=[Role.student]
    )
]


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/user")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/user/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"nonono"
    )
