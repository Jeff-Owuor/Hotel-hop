from crypt import methods
from . import main
from flask import redirect, render_template,url_for,flash
from .forms import SelectCountry,Book

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/country', methods = ['GET','POST'])
def country():
    country = SelectCountry()
    if country.validate_on_submit():
        category = country.category.data
        flash("Here are hotels from " + category)
        return redirect(url_for('main.hotel',category = category))

    
    return render_template('country.html', form = country)

@main.route('/hotel')
def hotel():
    

    return render_template('hotel.html')

@main.route('/bookSouth',methods= ['GET','POST'])
def bookSouth():
    book = Book()
    if book.validate_on_submit():
        In = book.In.data
        out = book.out.data
        return redirect(url_for('main.hotel',In= In,out = out))


    return render_template('book/bookSouth.html',book =book)    

@main.route('/bookLa')
def bookLa():

    return render_template('book/bookLa.html')  

@main.route('/bookMont')
def bookMont():

    return render_template('book/bookMont.html')  