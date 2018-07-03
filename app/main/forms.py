from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email







class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    '''
    class to create a form for creating a category
    '''
    name = StringField('Category  Name',validators=[Required()])
    submit = SubmitField('Create')

class PitchesForm(FlaskForm):
    '''
    class to create a wtf form for creating a pitch
    '''
    pitch = StringField('One Minute Pitch',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    '''
    Class to create a wtf form for creating a feedback on a pitch
    '''
    comment =  TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')