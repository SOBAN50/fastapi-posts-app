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

#=====================================================================================================================================

# For postgress tables, when we make tables through models.py, what it does is:
# If we reload/rerun our app, for example a table named "__tablename__ = users_table" which is defined in our models.py file
# What it would do is:  Check if a table named __tablename__ is present ===> If present, do nothing, if not create a new table.
# The issue is that if we want to update our table e.g add a new column :

# class Users_Table(Base):
#     __tablename__ = "completeapp_users_with_relation"
#     user_id = Column(Integer, nullable = False, primary_key = True)
#     email = Column(String, nullable = False, unique = True)

# TO

# class Users_Table(Base):
#     __tablename__ = "completeapp_users_with_relation"
#     user_id = Column(Integer, nullable = False, primary_key = True)
#     email = Column(String, nullable = False, unique = True)
#     contact = Column(Integer, nullable = True)

# What we would have to do is delete the previous table with all its data and reload/rerun the app so that it create a
# new table with the new column added. But that is not good. To address such issues and much more we use "ALEMBIC".
# Alembic also lets us keep track of all changes made to db (called revisions) and also undo changes if required.
# All revisions are stored in versions folder.

# STEP 1: Pip install alembic

# STEP 2: Initialize alembic that would create directories: alembic init <foldername_to_create>
# this command wil make a folder with the name 'foldername_to_create' and an alembic.ini file.
# the 'foldername_to_create' folder will hold all revision files and other data related to alembic for this specific app

# STEP 3: Configure the 'alembic/env.py' and 'alembic.ini' files according to your app
# procedure at https://www.youtube.com/watch?v=0sOvCWFmrtA at 10:36:00

# STEP 4: Make first revision i.e the first step in out posts app i.e create posts table in postgress. It will be done as
# alembic revision -m "create_posts_table"
# create_posts_table is the name os revision. All revisions are stored in versions folder as a .py file.
# ALMEBIC documentation for postgressql queries : https://alembic.sqlalchemy.org/en/latest/api/ddl.html

# Alembic would create a new table in postgress named "albemic_version" for its own use.

#=====================================================================================================================================

app.include_router(users.router)
app.include_router(posts.router)