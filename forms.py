from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,DateField
from wtforms.validators import InputRequired,DataRequired

username_required = "Please provide a username"
password_required = "Please provide a password"

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired(message=username_required)])
    password = PasswordField('Password',validators=[InputRequired(message=password_required)])
    remember = BooleanField(False)

class SignupForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    name = StringField('Fullname',validators=[DataRequired()])
    school = StringField('School',validators=[DataRequired()])
    dob = DateField('Date of Birth',validators=[DataRequired()])