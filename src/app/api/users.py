from typing import List
from fastapi import APIRouter, HTTPException, Path

from app.api import crud
from app.api.models import User, UserSchema

# get router obect to override api request handle
router = APIRouter()

# handle get all users request
@router.get("/", response_model=List[User])
async def get_all_users():
    return await crud.get_all()

# handle get user by id request
@router.get("/{id}/", response_model=User)
async def get_user(id: int = Path(..., gt=0),):
    user = await crud.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# handle add user request
@router.post("/", response_model=User, status_code=201)
async def create_user(payload: UserSchema):
    user_id = await crud.post(payload)

    response_object = {
        "Id": user_id,
        "Name": payload.Name,
    }
    return response_object

# handle update specific user request
@router.put("/{id}/", response_model=User)
async def update_user(payload: UserSchema, id: int = Path(..., gt=0),):
    user = await crud.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_id = await crud.put(id, payload)

    response_object = {
        "Id": user_id,
        "Name": payload.Name,
    }
    return response_object

# handle delete user request
@router.delete("/{id}/", response_model=User)
async def delete_user(id: int = Path(..., gt=0)):
    user = await crud.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await crud.delete(id)

    return user
