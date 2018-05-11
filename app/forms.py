from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired



class SomeForm(FlaskForm):
    msg_id = IntegerField('msg_id')
    # , validators=[IntegerField()]
    lenght = IntegerField('lenght')
    #remember_me = BooleanField('Remember Me ')
    submit = SubmitField('Get')

