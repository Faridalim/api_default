from fastapi import APIRouter

from .models import UserSchema, UserUpdateSchema
from app.db import database, db_users

router = APIRouter()


# ========== START ROUTE ADMIN ==================

@router.get("/")
async def get_all_users():
    query = db_users.select()
    notes = await database.fetch_all(query=query)
    return notes


@router.get("/{id_user}")
async def get_one_user(id_user: int):
    query = db_users.select().where(db_users.c.id == id_user)
    user = await database.fetch_one(query=query)
    print(user)
    return user


@router.post("/")
async def create_user(payload: UserSchema):
    query = db_users.insert().values(username=payload.username,
                                     password=payload.password,
                                     name=payload.name,
                                     role=payload.role,
                                     status=payload.status,
                                     info=payload.info
                                     ).returning(db_users)
    note = await database.fetch_one(query=query)
    return note


@router.put("/{id_user}")
async def edit_user(id_user: str, payload: UserUpdateSchema):
    query_user_db = db_users.select().where(db_users.c.id == id_user)
    user_db : UserSchema = await database.fetch_one(query=query_user_db)
    if payload.username != user_db.username:
        payload.username = user_db.username
    if payload.password != user_db.password:
        payload.password = user_db.password
        # belum selesai

    # user = await database.fetch_all(query=query)
    return user_db


@router.delete("/{id_user}")
async def delete_user(id_user: str):
    query = db_users.select()
    notes = await database.fetch_all(query=query)
    return notes
# ================ END ROUTE ADMIN ==============
