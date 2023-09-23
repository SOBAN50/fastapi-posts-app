from pydantic import BaseModel, EmailStr
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from datetime import datetime
from sqlalchemy.orm import relationship

Base = declarative_base()

class Users_Table(Base):
    __tablename__ = "users_table"
    user_id = Column(Integer, nullable = False, primary_key = True)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), server_default = text('Now()'))


class Posts_Table(Base):
    __tablename__ = "posts_table"
    post_id = Column(Integer, nullable = False, primary_key = True)
    user_id = Column(Integer, ForeignKey("users_table.user_id", ondelete="CASCADE"), nullable = False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = True)
    created_at = Column(TIMESTAMP(timezone=True), server_default = text('Now()'))
    ownership = relationship("Users_Table")

#-----------------------------------------------------------

class pydantic_users_createuser(BaseModel):
    email: EmailStr
    password: str

class pydantic_users_return_createuser(BaseModel):
    user_id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class pydantic_users_return_login(BaseModel):
    token: str
    token_type: str
    class Config:
        orm_mode = True

#-------------------

class pydantic_posts_createpost(BaseModel):
    title: str
    content: str

class pydantic_posts_return_createpost(BaseModel):
    user_id: int
    title: str
    content: str
    created_at: datetime
    ownership: pydantic_users_return_createuser
    class Config:
        orm_mode = True

class pydantic_posts_return_getone_getall(BaseModel):
    user_id: int
    title: str
    content: str
    created_at: datetime
    class Config:
        orm_mode = True

class pydantic_posts_return_updatepost(BaseModel):
    user_id: int
    title: str
    content: str
    class Config:
        orm_mode = True