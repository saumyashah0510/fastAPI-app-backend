from turtle import color
from sqlalchemy.sql.expression import null
from .database import BASE
from sqlalchemy import Column, ForeignKey,Integer,String,Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Post(BASE):
    __tablename__ = "post"
    
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,server_default='TRUE',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id", ondelete= "CASCADE"), nullable=False)
    
    owner = relationship("User") 
    
class User(BASE):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True,nullable=False)    
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
class Vote(BASE):
    __tablename__ = "votes"
    
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id = Column(Integer,ForeignKey("post.id",ondelete="CASCADE"),primary_key=True)    