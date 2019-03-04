from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    post_blog=db.relationship('Post_blog', backref='user',lazy='dynamic')
    comment=db.relationship('Comments', backref='user', lazy='dynamic') 
    password_secure = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    


    @property
    def password(self):
       raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
      self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
     return check_password_hash(self.pass_secure,password)       

    def __repr__(self):
        return f'User {self.username}'


       
class Post_blog(db.Model):
    __tablename__ = 'post_blog'

    id = db.Column(db.Integer,primary_key = True)
    post_blog = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comments',backref = 'post_blog',lazy="dynamic")

    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(id):
        blog = Post_blog.query.all()
        return blog
        
        def delete_post(self,id):
             comments = Comments.query.filter_by(id = id).all()
        for comments in comments:
             db.session.delete(comment)
             db.session.commit()
             db.session.delete(self)
             db.session.commit()
    def __repr__(self):
        return f'User {self.name}'   

   

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    post_blog_id = db.Column(db.Integer,db.ForeignKey('post_blog.id'))
    

    def __repr__(self):
        return f'User {self.name}'    

    def delete_comment(self):
       db.session.delete(self)
       db.session.commit()

          
class subscription(db.Model):
    __tablename__ = 'subsription'

    id = db.Column(db.Integer,primary_key = True)
    name= db.Column(db.String(255))
    email=db.Column(db.String(255))
  

class Quote:
    '''
    quote class to define quote Objects
    '''

    def __init__(self,id, author, content):
        self.id =id
        self.author = author
        self.content= content
        
       



