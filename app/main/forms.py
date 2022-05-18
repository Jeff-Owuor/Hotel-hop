from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SelectField,SubmitField,DateField,StringField

class SelectCountry(FlaskForm):
     category = SelectField('Countries', choices=[('Choose...','Choose...'),('South Africa','South Africa'),('Egypt','Egypt'),('Zanzibar','Zanzibar'),('Tanzania','Tanzania'),('Madagascar','Madagascar')],validators=[DataRequired()])
     next = SubmitField("Continue")
class Book(FlaskForm):
     In = DateField('Check-in:')
     out = DateField('Check-out:')
     adults = StringField('Adults:')
     children =StringField('Children:')
     book = SubmitField('Book')
