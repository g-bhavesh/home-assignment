from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    Name: str = Field(..., min_length=2, max_length=50)

class User(UserSchema):
    Id: int
