from app.api.models import UserSchema
from app.db import users, database

# insert user payload to db
async def post(payload: UserSchema):
    query = users.insert().values(Name=payload.Name)
    return await database.execute(query=query)

# get user details from db based on id
async def get(id: int):
    query = users.select().where(id==users.c.Id)
    return await database.fetch_one(query=query)

# get all users details from db
async def get_all():
    query = users.select()
    return await database.fetch_all(query=query)

# update specific user details based on provided id
async def put(id: int, payload: UserSchema):
    query = (
        users
        .update()
        .where(id==users.c.Id)
        .values(Name=payload.Name)
        .returning(users.c.Id)
    )
    return await database.execute(query=query)

# delete specific user details based on provided id
async def delete(id: int):
    query = users.delete().where(id==users.c.Id)
    return await database.execute(query=query)
