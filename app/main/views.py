
from flask_login import login_user,logout_user,login_required
from flask import render_template,request,flash,redirect,url_for,abort
from ..models import  User,Comments,subscription
from flask_login import login_required,current_user
from ..email import mail_message


from .forms import UpdateProfile
from . import main
from .forms import  BlogForm,SubscriptionForm,AddPostForm,CommentForm
from ..models import User,Post_blog
from flask_login import login_user
from .. import db,photos
from ..request import get_quote









# Views
@main.route('/',methods = ['GET','POST'])
def index():
    all_blogs=Post_blog.get_blogs()
 
    title = 'Home - Welcome to The best Movie Review Website Online'
    # return render_template('index.html', title = title , )


    form=SubscriptionForm()
    if form.validate_on_submit():
          name = form.name.data

          email= form.email.data
          new_subscriber=subscription(name=name,email=email)
          db.session.add(new_subscriber)
          db.session.commit()

          mail_message("Thanks!","email/welcome_user",new_subscriber.email,user=new_subscriber)

          return redirect(url_for('main.index'))
    quote=get_quote()
    posts=Post_blog.get_blogs()
    title="Home| Welcome to blog"

    return render_template('index.html',title=title,quote=quote,posts=posts,form=form,all_blogs=all_blogs)
 





@main.route('/newblogs/',methods = ['GET','POST'])
@login_required
def newblogs():

    # form = blogForm()
      form=SubscriptionForm()
      if form.validate_on_submit():
        name = form.name.data
        email= form.email.data
        new_subscriber=Subscription(name=name,email=email)
        db.session.add(new_subscriber)
        db.session.commit()
        mail_message("Thans","email/welcome_user",new_subscriber.email,user=new_subscriber)
        return redirect(url_for('main.index'))
      quote=get_quote()
      posts=Post_blog.get_blogs()
      title="Home| Welcome to blog"
      return render_template('index.html',title=title,quote=quote,posts=posts,subscription_form=form)
        # blogs= form.Post_blog.data

        # Updated review instance
      newblogs= Post_blog( Post_blog= blogs,user_id=current_user.id)

        # save review method
      newblogs.save_blogs()
      return redirect(url_for('.index',blogs = blogs))
   
    # return render_template('newblogs.html',newblogs=form)









@main.route('/post/<int:id>')
def single_post(id):
    post=Post.query.filter_by(id=id).first()
    comments=Comments.get_comments(id=id)
    return render_template('single_post.html',post=post,comments=comments)   




  
@main.route('/post/new', methods = ['GET', 'POST'])
@login_required
def add_post():
    form = AddPostForm()
    
    if form.validate_on_submit():
        # title = form.title.data

        post_blog= form.post_blog.data
       

        new_post = Post_blog(post_blog=post_blog)
        new_post.save_blog()

        
       

        return redirect(url_for('main.index'))

    

    title = 'Add Post| blogs'    
    return render_template('post.html', title = title, post_form = form)

@main.route('/new/comment/<int:id>', methods = ['GET','POST'])
def add_comment(id):
  post= Post_blog.query.filter_by(id=id).first()
  if post is None:
    abort(404)

  form=CommentForm()
  if form.validate_on_submit():
     comment=form.comment.data
     new_comment=Comments(comment=comment,post_blog=post)
     db.session.add(new_comment)  
     db.session.commit() 

  comment=Comments.query.filter_by(post_blog_id=id).all()   
     
  
  return render_template('comment.html',comments=comment, comment_form=form)



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
























