from .import db;
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


class User(UserMixin,db.Model):
    '''
    User class to define a user in the database
    '''
    #Table name
    __tablename__ = 'users'

    #id column(primary key)
    id=db.Column(db.Integer,primary_key = True)

    #username column for usernames
    name = db.Column(db.String(100))
    #email column for a user's email address
    email = db.Column(db.String(100),unique = True, index=True)

    #password column for passwords
    password = db.Column(db.String(100))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.name}'

