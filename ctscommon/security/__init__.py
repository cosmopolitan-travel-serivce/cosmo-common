from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from ctscommon.security.models import CTSUser

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/")


async def get_connected_user(token: str = Depends(oauth2_scheme)):
    return fake_decode_token(token)


def fake_decode_token(token):
    return CTSUser(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )
