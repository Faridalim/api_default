from pydantic import BaseModel, Field, constr, Json
from typing import List, Optional
from enum import Enum

class RoleSchema(str, Enum):
    admin   = "admin"
    user    = "user"

class StatusSchema(str, Enum):
    active      = "active"
    inactive    = "inactive"
    deleted     = "deleted"

class UserSchema(BaseModel):
    username:   constr(max_length=300, min_length=5)
    password:   constr(max_length=300, min_length=5)
    name:       constr(max_length=300, min_length=5)
    role:       List[RoleSchema] = ["user"]
    status:     StatusSchema
    info:       dict

    class Config:
        orm_mode = True

class UserUpdateSchema(BaseModel):
    username:   Optional[constr(max_length=300, min_length=5)]
    password:   Optional[constr(max_length=300, min_length=5)]
    name:       Optional[constr(max_length=300, min_length=5)]
    role:       List[RoleSchema] = ["user"]
    status:     Optional[StatusSchema]
    info:       Optional[dict]

    class Config:
        orm_mode = True