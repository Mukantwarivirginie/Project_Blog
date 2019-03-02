
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField,BooleanField
from wtforms.validators import Required
from wtforms import ValidationError




# class ReviewForm(FlaskForm):

#     title = StringField(' title',validators=[Required()])
#     review = TextAreaField(' review', validators=[Required()])
#     submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')   



class BlogForm(FlaskForm):

    
    blog = TextAreaField(' blog', validators=[Required()])
    submit = SubmitField('Submit')
