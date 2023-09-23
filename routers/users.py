from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

import models
from database import get_db
from oauth2 import create_access_token, get_current_user

router = APIRouter(tags = ['Users'])


@router.post("/users/signup", status_code = status.HTTP_201_CREATED, response_model = models.pydantic_users_return_createuser)
def register_user(input_credentials: models.pydantic_users_createuser, db: Session = Depends(get_db)):
    
    hashed_password = pwd_context.hash(input_credentials.password)
    input_credentials.password = hashed_password

    new_user = models.Users_Table(**input_credentials.dict())
    db.add(new_user); db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/users/login", response_model = models.pydantic_users_return_login)
def login_user(input_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    res = db.query(models.Users_Table).filter(models.Users_Table.email == input_credentials.username).first()
    if not res:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = f'Username {input_credentials.username} not found')
    
    is_password_same = pwd_context.verify(input_credentials.password, res.password)
    if not is_password_same:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = 'Invalid Credentials')

    access_token = create_access_token(data = {"user_id": res.user_id})
    return {'token': access_token, 'token_type': 'bearer'}