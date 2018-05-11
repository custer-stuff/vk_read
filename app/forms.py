from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired



class SomeForm(FlaskForm):
    msg_id = StringField('msg_id', validators=[DataRequired()])
    lenght = StringField('lenght')
    #remember_me = BooleanField('Remember Me ')
    submit = SubmitField('Sign in')
