from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from typing import List

import models
from oauth2 import get_current_user
from database import get_db

router = APIRouter(tags = ['Posts'])

# Here 'pydantic_posts_return_createpost' will also return user info (which is ofcourse not present in posts table but users table).
@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model = models.pydantic_posts_return_createpost)
def create_post(input_post: models.pydantic_posts_createpost, db: Session=Depends(get_db), current_user = Depends(get_current_user)):
    new_post = models.Posts_Table(user_id = current_user.id, **input_post.dict())
    db.add(new_post); db.commit()
    db.refresh(new_post)
    return new_post

#------------------------------------------

@router.get("/posts", response_model = List[models.pydantic_posts_return_getone_getall])
def get_all_posts(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    res = db.query(models.Posts_Table).filter(models.Posts_Table.user_id == current_user.id).all()
    return res

#------------------------------------------

@router.get("/posts/{input_id}", response_model = models.pydantic_posts_return_getone_getall)
def get_single_post(input_id : int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    res = db.query(models.Posts_Table).filter((models.Posts_Table.user_id == current_user.id) & (models.Posts_Table.post_id == input_id)).first()
    if not res:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Post with id {input_id} not found')
    return res

#------------------------------------------

@router.put("/posts/{input_id}", response_model = models.pydantic_posts_return_updatepost)
def update_post(input_id: int, input_post: models.pydantic_posts_createpost, db: Session=Depends(get_db), current_user=Depends(get_current_user)):
    
    query = db.query(models.Posts_Table).filter((models.Posts_Table.user_id == current_user.id) & (models.Posts_Table.post_id == input_id))
    query_res = query.first()

    if not query_res:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Post with id {input_id} not found')
    
    query.update(input_post.dict(), synchronize_session = False)
    db.commit()

    return query.first()

#------------------------------------------

@router.delete("/posts/{input_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(input_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):

    query = db.query(models.Posts_Table).filter((models.Posts_Table.user_id == current_user.id) & (models.Posts_Table.post_id == input_id))
    query_res = query.first()

    if not query_res:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Post with id {input_id} not found')
    
    query.delete(synchronize_session = False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)