from fastapi.security import OAuth2PasswordBearer

TOKEN_URL = "/api/auth/token"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN_URL)
optional_oauth2_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN_URL, auto_error=False)
