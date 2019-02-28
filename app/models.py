from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
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
    password_secure = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitches',backref = 'pitches',lazy="dynamic")


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
       
class Pitches(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comments',backref = 'commen',lazy="dynamic")


    @classmethod
    def get_pitches(cls):
       pitches = Pitches.query.filter_by().all()
       return pitches
        
        
         
    def __repr__(self):
        return f'User {self.name}'       

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    

    def __repr__(self):
        return f'Pitches {self.name}'           



