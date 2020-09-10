from app.api import users
from app.db import database, engine, metadata
from fastapi import FastAPI

# create user table
metadata.create_all(engine)

# init fastapi app instance
app = FastAPI()

# handle app events
# on startup
@app.on_event("startup")
async def startup():
    await database.connect()

# on shutdown
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# bind api to router
app.include_router(users.router, prefix="/users", tags=["users"])
