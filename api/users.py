from fastapi import APIRouter, status, Depends
from typing import Dict, Any
from fastapi.exceptions import HTTPException
from api import routes
from schema import Health, User, UserDict
from zarda.zin import Zarda

router = APIRouter(tags=["users"])


@router.get(routes.HEALTH, response_model=Health)
def health_check() -> Health:
    return Health(status="OK", description="API is reachable")


@router.post(routes.ENTER_INFO)
def enter_info(*, user: User, z: Zarda = Depends(Zarda)):
    z.add_users(user.name, user.spent)
    return user
