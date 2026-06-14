from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField
from wtforms.validators import InputRequired,EqualTo

class RegistrationForm(FlaskForm):
    user = StringField("Username:",validators=[InputRequired()])
    password = StringField("Password:",validators=[InputRequired()])
    password2 = StringField("Confirm password:",validators=[InputRequired(),EqualTo()])
    submit= SubmitField("Submit")