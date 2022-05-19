from flask import render_template
from . import main
from .forms import ReviewsForm

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template("index.html")

@main.route("/review")
def new_review():
    '''
       Function to add a review
    '''
    form = ReviewsForm()
    return render_template('review.html',form = form)