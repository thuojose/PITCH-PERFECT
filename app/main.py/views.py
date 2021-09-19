from flask import render_template
from ..models import Pitch
from . import main
@main.route('/',)
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