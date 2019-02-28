from flask_login import login_user,logout_user,login_required
from flask import render_template,request,redirect,url_for,abort
from ..models import  User


from flask_login import login_required,current_user
from . import main
# from ..request import get_movies,get_movie,search_movie
from .forms import ReviewForm, PitchForm
# from ..models import Review
from flask import render_template,redirect,url_for
from ..models import User
# from .forms import RegistrationForm

from .forms import ReviewForm,UpdateProfile
from .. import db

from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user
from ..models import User,Pitches
# from .forms import LoginForm,RegistrationForm
from .. import db,photos







# Views
@main.route('/')
def index():
      all_pitches = Pitches.get_pitches()



      title = 'Home - Welcome to The best Movie Review Website Online'



      return render_template('index.html', title = title , pitches=all_pitches)
@main.route('/pitch')
@login_required
def add_pitch():
    form = PitchForm()
    if form .validate_on_submit():
         category = form.content.data
         new_pitch = pitch(content=pitch,category = category, user=current_user)
         new_pitch.save_pitch()
         return redirect(url_for('main.index'))
    #  all_pitches = pitch.get_pitches()
    title='cause'
    return render_template('pitches.html',title = title,pitch_form = form,user=current_user)













@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)  




@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))  