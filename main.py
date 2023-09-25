from fastapi import FastAPI
from routers import users, posts
import models
from database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware

#----- This is no longer needed when we are using alembic -----
models.Base.metadata.create_all(bind = engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(posts.router)