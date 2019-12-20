from datetime import datetime, timedelta
from typing import List, Optional

import jwt
from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from jwt import PyJWTError
from starlette.status import HTTP_401_UNAUTHORIZED

from ctscommon.config.loader import get_config
from ctscommon.security import oauth2_scheme, optional_oauth2_scheme
from ctscommon.security.models import CTSUser

default_jwt_secret_key = None
SECRET_KEY = get_config("JWT_SECRET_KEY", default_jwt_secret_key)
ALGORITHM = get_config("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(get_config("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30))
_CONFIG_LOADED = False


def load_all_config():
    global SECRET_KEY
    global ALGORITHM
    global ACCESS_TOKEN_EXPIRE_MINUTES
    global _CONFIG_LOADED
    if _CONFIG_LOADED is False:
        SECRET_KEY = get_config("JWT_SECRET_KEY", default_jwt_secret_key)
        ALGORITHM = get_config("JWT_ALGORITHM", "HS256")
        ACCESS_TOKEN_EXPIRE_MINUTES = int(get_config("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30))
        _CONFIG_LOADED = True


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
old_pwd_context = CryptContext(schemes=["django_pbkdf2_sha256"], deprecated="auto")


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def verify_old_password(plain_password, hashed_password) -> bool:
    return old_pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(user: CTSUser, expires_delta: timedelta = None):
    load_all_config()
    to_encode = user.dict()
    if not expires_delta:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user_optional(token: str = Depends(optional_oauth2_scheme)) -> Optional[CTSUser]:
    if token:
        return await get_current_user(token)
    return None


async def get_current_user(token: str = Depends(oauth2_scheme)) -> CTSUser:
    load_all_config()
    credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        decode_options = {}
        # TODO check expiration date of token or add options = {"verify_exp": True} option jwt.decode
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], options=decode_options)
        username: str = payload.get("username")
        email: str = payload.get("email")
        permissions: List[str] = payload.get("permissions")
        managed_customers: List[str] = payload.get("managed_customers")
        customer: str = payload.get("customer")
        offices: List[str] = payload.get("offices")
        is_cts_staff: bool = payload.get("is_cts_staff")
        is_agency_admin: bool = payload.get("is_agency_admin")
        force_change_password: bool = bool(payload.get("force_change_password"))
        full_name: str = payload.get("full_name")
        impersonator: str = payload.get("impersonator")
        # expiration_date: str = payload.get("exp")
        if username is None:
            raise credentials_exception
        user = CTSUser(username=username, email=email, full_name=full_name, customer=customer, permissions=permissions,
                       managed_customers=managed_customers, offices=offices, is_cts_staff=is_cts_staff,
                       is_agency_admin=is_agency_admin, force_change_password=force_change_password,
                       impersonator=impersonator)
    except PyJWTError:
        raise credentials_exception
    if user is None:
        raise credentials_exception
    return user
