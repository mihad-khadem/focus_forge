from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
# user schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):

    password: str
    is_active: bool = True
    is_superuser: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class UserPublic(UserBase):
    id: str = Field(..., alias="_id")
    is_active: bool = True
    is_superuser: bool = False

    class Config:
        orm_mode = True
        allow_population_by_field_name = True