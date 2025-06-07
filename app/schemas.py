from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel,EmailStr, conint


class UserOut(BaseModel):
    email: EmailStr
    id: int    
    created_at: datetime
    
    class Config:
        from_attributes = True

class PostBase(BaseModel):
    title: str 
    content: str    
    published : bool = True
    

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    class Config:
        from_attributes = True   
         
class UserCreate(BaseModel): 
    email: EmailStr
    password: str
        
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str        
    
class Token(BaseModel):
    access_token : str
    token_type : str
    
class TokenData(BaseModel):
    id : Optional[str] = None        
    
class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, conint(le=1)]