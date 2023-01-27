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


class ZardaBD(ZardaBase):
    number_users = int
    username = str
    balance = float
    zarda_name = str


class User(BaseModel):
    name: str
    spent: float


class UserDict(BaseModel):
    users: Union[str, None] = None


class ZardaName(BaseModel):
    name: str
    num_users: int


class Health(BaseModel):
    status: str
    description: str
