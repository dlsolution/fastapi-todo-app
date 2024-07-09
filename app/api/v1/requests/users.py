from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    email: str = Field(min_length=1, max_length=255)
    password: str = Field(min_length=8)

class UserLogin(BaseModel):
    email: str = Field(min_length=1, max_length=255)
    password: str = Field(min_length=8)
