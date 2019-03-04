
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField,BooleanField
from wtforms.validators import Required
# from wtforms import ValidationError




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









class AddPostForm(FlaskForm):
    # title=StringField('Title',validators = [Required()])
    post_blog=TextAreaField('Content',validators = [Required()])
    # image=StringField('Image url',validators = [Required()])
    submit=SubmitField('SUBMIT')

class CommentForm(FlaskForm):
   
   username = StringField('Enter your name',validators=[Required()])
   comment = TextAreaField('blog comment', validators=[Required()])
   submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class SubscriptionForm(FlaskForm):
    name=StringField('Name',validators =[Required()])
    email=StringField('Email',validators =[Required()])
    submit = SubmitField('Submit')

class UpdatePostForm(FlaskForm):
    title=StringField('Title',validators = [Required()])
    content=TextAreaField('Content',validators = [Required()])
    submit=SubmitField('SUBMIT')





# class SubscriptionForm(FlaskForm):

    
#    Subscription  = TextAreaField('Subscription ', validators=[Required()])
#    submit = SubmitField('Submit')

