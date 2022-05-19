from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired


class ReviewsForm(FlaskForm):
    review = TextAreaField('Tell us about your stay', validators=[DataRequired()])
    submit = SubmitField('Submit')
