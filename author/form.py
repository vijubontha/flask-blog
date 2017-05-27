from flask_wtf import Form
from wtforms import validators,StringField,PasswordField
from wtforms.fields.html5 import EmailField

class RegisterForm(Form):
    
    fullname=StringField('Full Name',[validators.Required()])
    email=EmailField('Email',[validators.Required()])
    username=StringField('username',[
        validators.Required(),
        validators.length(min=4,max=25)
        ])           
    password=PasswordField('New Password',[
        validators.Required(),
        validators.EqualTo('confirm',message='Password must match'),
        validators.length(min=4,max=80)
        ])
    confirm=PasswordField('Repeat Password')
    
class LoginForm(Form):
    username=StringField('username',[
        validators.Required(),
        validators.Length(min=4,max=25)
        ])
    password=PasswordField('Password',[
        validators.Required(),
        validators.Length(min=4,max=25)
        ])