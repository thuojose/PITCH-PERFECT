from flask import render_template
from . import main
@main.route('/',)
def index():
    '''
    View root page function that returns the index page and it's data
    '''
    return render_template('home.html')