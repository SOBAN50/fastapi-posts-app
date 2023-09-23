from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi import HTTPException, status

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7" # any random long text
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode['exp'] = expire
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt

#--------------------------------------------------------------------

from pydantic import BaseModel
from typing import Optional

class pydantic_TokenData(BaseModel):
    id: Optional[str] = None

# verify if provided jwt token is correct
def verify_jwt_token(jwt_token: str, credentials_exception):
    try:
        payload = jwt.decode(jwt_token, SECRET_KEY, algorithms = [ALGORITHM])
        
        token_returned_id: str = payload.get("user_id")
        if not token_returned_id:
            raise credentials_exception
        
        token_data = pydantic_TokenData(id = token_returned_id)

    except JWTError:
        raise credentials_exception
    
    return token_data
    
#--------------------------------------------------------------------

from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'users/login')

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail = 'Could not validate Credentials',
                                          headers = {"WWW-Authenticate": "Bearer"})
    return verify_jwt_token(token, credentials_exception)


