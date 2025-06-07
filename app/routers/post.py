from .. import models,schemas, oauth2
from fastapi import APIRouter,FastAPI,Response,status,HTTPException,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional

router = APIRouter(
    prefix = "/posts",
    tags = ['Posts']
)

@router.get("/", response_model=List[schemas.Post])
def get_posts(db : Session = Depends(get_db),curr_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post : schemas.PostCreate, db : Session = Depends(get_db),
                 curr_user: int = Depends(oauth2.get_current_user)): #post is a pydantic model

    new_post = models.Post(owner_id = curr_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}",response_model=schemas.Post)
def get_post(id : int,db : Session = Depends(get_db),curr_user: int = Depends(oauth2.get_current_user)):

    test_post = db.query(models.Post).filter(models.Post.id == id).first()
 
    if not test_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id : {id} was not found")
        
    return test_post
  
  
    
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)    
def delete_post(id : int,db : Session = Depends(get_db),curr_user: int = Depends(oauth2.get_current_user)):
    
    deleted_post_query = db.query(models.Post).filter(models.Post.id == id)
    deleted_post = deleted_post_query.first()
    
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    if deleted_post.owner_id != curr_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")    

    deleted_post_query.delete(synchronize_session = False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}",response_model=schemas.Post)
def update_post(id : int , post:schemas.PostUpdate , db : Session = Depends(get_db),curr_user: int = Depends(oauth2.get_current_user)):
    
    updated_query = db.query(models.Post).filter(models.Post.id == id)
    
    updated_post = updated_query.first()
    
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    if updated_post.owner_id != curr_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
        
    updated_query.update(post.dict(),synchronize_session=False)
    db.commit()
    
    return updated_query.first()