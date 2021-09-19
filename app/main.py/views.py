from flask import render_template, redirect, url_for
from ..models import Pitch, User, Comment, Upvote, Downvote
from flask_login import login_required, current_user
from .forms import PitchForm,CommentForm
from . import main
from .. import db
@main.route('/',methods = ['GET', 'POST'])
def index():
    '''
    View root page function that returns the index page and it's data
    '''
    title = 'Last Pitch'
    descr = 'The Last Pitch application allows users to submit their one minute pitches and other users will vote on them and leave comments to give their feedback. The pitches are organized by category.'
    pitch = Pitch.query.filter_by().first()
    pickuplines = Pitch.query.filter_by(category='pickuplines')
    interviewpitch = Pitch.query.filter_by(category='interviewpitch')
    promotionpitch = Pitch.query.filter_by(category='promotionpitch')
    productpitch = Pitch.query.filter_by(category='productpitch')
    
    return render_template('home.html',title= title,intro = descr, pitch = pitch, pickuplines = pickuplines, interviewpitch = interviewpitch, promotionpitch = promotionpitch, productpitch = productpitch)

@main.route('/pitches/new/', methods = ['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        # print(current_user._get_current_object().id, title = title,description=description,category=category)
        new_pitch = Pitch(owner_id=current_user._get_current_object().id, title=title, description=description, category
        =category)
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('pitches.html', form=form)

@main.route('/comment/new/<int:pitch_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.new_comment', pitch_id = pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comments.html', form = form, comment = all_comments, pitch = pitch)
