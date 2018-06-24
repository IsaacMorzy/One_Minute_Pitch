from .import db

class User():
    '''
    User class to define a user in the database
    '''
    #Table name
    __tablename__ = 'users'

    #id column(primary key)
    id=db.Column(db.integer,primary_key = True)

    #username column for usernames
    username = db.column(db.String(100))

    #email column for a user's email address
    email = db.column(db.String(100),unique = True, index=True)

    #password_hash column for passwords
    password_hash = db.column(db.String(100))

    def __repr__(self):
        return f'User {self.username}'