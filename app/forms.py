from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, Label
from wtforms.validators import DataRequired


class SomeForm(FlaskForm):
    msg_id = IntegerField('msg_id')
    # , validators=[IntegerField()]
    length = IntegerField('length')
    # remember_me = BooleanField('Remember Me ')
    submit = SubmitField('Get')
    msg_body = StringField('msg_body')
    msg_text = StringField('msg_text')
