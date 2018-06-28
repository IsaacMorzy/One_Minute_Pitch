from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from .import login_manager
from datetime import datetime





@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(int(user_id))
class User(UserMixin,db.Model):
    '''
    User class to define a user in the database
    '''
    #Table name
    __tablename__ = 'users'

    #id column(primary key)
    id=db.Column(db.Integer,primary_key = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    #username column for usernames
    name = db.Column(db.String(100))
    #email column for a user's email address
    email = db.Column(db.String(100),unique = True, index=True)

    #password column for passwords
    password_hash= db.Column(db.String(100))
    profile_pic_path = db.Column(db.String()) 
    bio = db.Column(db.String(100))  
    photos = db.relationship('PhotoProfile',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.name}'

class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

class Category(db.Model):
    '''
    category class to define the categories of pitches
    '''
    __tablename__ = 'categories'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    pitches= db.relationship('Pitch', backref='category', lazy='dynamic')

    def save_category(self):
        '''
        function that saves a new category to the category's table
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        '''
        function that queries the category table 
        returns:
            categories:all the details in the category table
        '''
        categories = Category.query.all()
        return categories

class Pitch(db.Model):
    '''
    Pitch class to define pitches
    '''
    __tablename__ = 'pitches'
    id =  db.Column(db.Integer,primary_key= True)
    pitch = db.Column(db.String(100))
    category_id= db.Column(db.Integer,db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    def save_pitch(self):
        '''
        functon that saves a new pitch to the pitches
        '''
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_pitches(cls,category_id):
            '''
            Function that queries the pitches table in the database
            Args:
                category_id : specific category_id
             Returns:
                pitches:pitches with the specific category_id
                '''
            pitches = Pitch.query.order_by(Pitch.id.desc()).filter_by(category_id=category_id).all()

            return pitches