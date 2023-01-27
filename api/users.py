from fastapi import APIRouter, Depends

from fastapi.exceptions import HTTPException
from api import routes
from sql.models import User
from sqlalchemy.orm import Session
from schema import Health, User, UserDict, ZardaName
from zarda.zin import Zarda

router = APIRouter(tags=["users"])


@router.get(routes.HEALTH, response_model=Health)
def health_check() -> Health:
    return Health(status="OK", description="API is reachable")


# @router.post(routes.ENTER_INFO, response_model=UserDict)
# def enter_users(*, user: User, z: Zarda = Depends(Zarda)) -> UserDict:
#
#     return z.users


@router.post(routes.ZARDA_NAME, response_model=ZardaName)
def enter_name(*, zarda_name: ZardaName, z: Zarda = Depends(Zarda)) -> ZardaName:
    if not z.zarda_name and z.num_users:
        raise HTTPException(status_code=403, detail="zardas name is missing")
    z.zarda_name = zarda_name.name
    z.num_users = zarda_name.num_users
    return ZardaName(name=z.zarda_name, num_users=z.num_users)
