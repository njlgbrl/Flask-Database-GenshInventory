from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.validators import InputRequired

class loginForm(Form):
    username = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])

class registerForm(Form):
    email = StringField('E-mail Address', [InputRequired()])
    username = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired(), validators.EqualTo('repeatPassword', message='Password must match')])
    repeatPassword = PasswordField('Repeat Password', [InputRequired()])