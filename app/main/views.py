from ..models import User,PhotoProfile,Category,Pitch
from . import main
from flask import render_template,request,redirect,url_for,abort
from .forms import CategoryForm,PitchesForm,UpdateProfile
from flask_login import login_required,current_user
from ..import db,photos



#....

@main.route('/')
def index():
    '''
    function that renders the index page
    '''
    title = 'Home'

    categories  = Category.get_categories()
    return render_template('index.html',title = title,categories=categories)

@main.route('/category/new',methods=['GET','POST'])
@login_required
def new_category():
    '''
    function that returns a page with a form to create a new category
    '''
    form  = CategoryForm()

    if form.validate_on_submit():
        name = form.name.data
        new_category = Category(name=name)
        new_category.save_category()
        return redirect(url_for('.index'))
        title = 'New Category'
    return render_template('new_category.html',title=title,category_form=form)

@main.route('/category/<int:id>')
def category(id):

    '''
    View group route function that returns a list of pitches in the route and allows a user to create a pitch for the selected route
    '''
    category = Category.query.get(id)

    if category is None:
        abort(404)

    pitches = Pitch.get_pitches(id)
    title = f'{category.name} page'

    return render_template('category.html', title=title, category=category, pitches=pitches)

@main.route('/category/pitch/new/<int:id>',methods=['GET','POST'])
@login_required
def new_pitch(id):
    '''
    View new pitch route function that returns a page with a form to create a pitch for the specified category
    '''
    form = PitchesForm()
    category = Category.query.filter_by(id=id).first()
    if category is None:
        abort(404)

    if form.validate_on_submit():
        pitch= form.pitch.data
        new_pitch = Pitch(pitch=pitch,category=category,user_id=current_user.id)
        new_pitch.save_pitch()
        return redirect(url_for('.category',id=category.id))

    title='New Pitch'
    return render_template('new_pitch.html',title=title,pitch_form=form,category=category)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(name = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user )

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(name = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.name))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(name = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        user_photo = PhotoProfile(pic_path = path,user = user)
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))




