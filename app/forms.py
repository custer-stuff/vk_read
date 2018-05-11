from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired



class SomeForm(FlaskForm):
    username = StringField('msg_id', validators=[DataRequired()])
    password = StringField('lenght', validators=[DataRequired()])
    #remember_me = BooleanField('Remember Me ')
    submit = SubmitField('Sign in')
