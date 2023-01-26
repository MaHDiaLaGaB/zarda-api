from pydantic import BaseModel
from typing import Union


class ZardaBase(BaseModel):
    class Config:
        orm_mode = True
        extra = "forbid"
        use_enum_values = True
        anystr_strip_whitespace = True
        validate_all = True
        validate_assignment = True
        allow_inf_nan = False


class User(ZardaBase):
    name: str
    spent: float


class UserDict(ZardaBase):
    users: Union[str, None] = None


class ZardaName(ZardaBase):
    name: str
    num_users: int


class Health(ZardaBase):
    status: str
    description: str
