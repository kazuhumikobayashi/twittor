from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String

from flaskr import db
from sqlalchemy.orm import relationship
from pymysql.constants.FLAG import AUTO_INCREMENT

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(16))
    password = Column(String(32))
    
    def __repr__(sewlf):
        return '<User id={id} user_name={user_name} password={password}>'.format(
                id=self.id, product_name=self.product_name, password=self.password)

class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String(128))
    user = relationship("User")

    def __repr__(self):
        return '<Post id={id} post_user_id={post_user_id} content={content} post_date={post_date}>'.format(
                id=self.id, post_user_id=self.post_user_id, content=self.content, post_date=self.post_date)

class Follower(db.Model):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    follower_user_id =  Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User")
    follower_users = relationship("User")

    def __repr__(self):
        return '<Follower id={id} user_id={user_id} follower_user_id={follower_user_id}>'.format(
                id=self.id, user_id=self.user_id, follower_user_id=self.follower_user_id)
