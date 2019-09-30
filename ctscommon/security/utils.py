from datetime import datetime, timedelta
from typing import List

import jwt
from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from jwt import PyJWTError
from starlette.status import HTTP_401_UNAUTHORIZED

from ctscommon.config.loader import get_config
from ctscommon.security import oauth2_scheme, CTSUser

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = get_config("JWT_SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")
ALGORITHM = get_config("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(get_config("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30))


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(user: CTSUser, expires_delta: timedelta = None):
    to_encode = user.dict()
    if not expires_delta:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)) -> CTSUser:
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
        # expiration_date: str = payload.get("exp")
        if username is None:
            raise credentials_exception
        user = CTSUser(username=username, email=email, full_name=None, customer=customer, permissions=permissions,
                       managed_customers=managed_customers, offices=offices, is_cts_staff=is_cts_staff, is_agency_admin=is_agency_admin)
    except PyJWTError:
        raise credentials_exception
    if user is None:
        raise credentials_exception
    return user
