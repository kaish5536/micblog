# coding: utf-8
from flask_wtf import Form
from wtforms import TextField,BooleanField,PasswordField
from wtforms.validators import Required

class LoginForm(Form):
    name = TextField('Name',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    rememder_me=BooleanField('Remember_me',default=False)
