from fastapi import FastAPI
from app.db import engine, database, metadata
from app.d_user import users
from app.d_vaksin import vaksin

metadata.create_all(engine)

app = FastAPI()

# @app.on_event("startup")
# async def startup():
#     await database.connect()
#     print("db connected")
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()
#     print("db disconnected")

@app.get("/")
async def index():
    return "bismillah"

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(vaksin.router, prefix="/vaksin", tags=["vaksin"])