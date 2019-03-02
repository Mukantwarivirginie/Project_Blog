
from flask_login import login_user,logout_user,login_required
from flask import render_template,request,flash,redirect,url_for,abort
from ..models import  User
from flask_login import login_required,current_user
from . import main
from .forms import  BlogForm
from ..models import User,Post_blog
from flask_login import login_user
from .. import db,photos









# Views
@main.route('/')
def index():
      all_Post_blog=Post_blog .get_blog()



      title = 'Home - Welcome to The best Movie Review Website Online'



      return render_template('index.html', title = title , all_Post_blog=all_Post_blog)


@main.route('/newblog/',methods = ['GET','POST'])
@login_required
def newblog():

    form = blogForm()
  
    if form.validate_on_submit():
       
        pitch= form.Post_blog.data

        # Updated review instance
        newpitch = Post_blog( Post_blog= blog,user_id=current_user.id)

        # save review method
        newblog.save_blog()
        return redirect(url_for('.index',blog = blog))

   
    return render_template('newblog.html',newblog=form)






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



