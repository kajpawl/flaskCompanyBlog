from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    name = StringField('Your name: ', validators=[DataRequired('Please enter your first name.')])
    surname = StringField('Your surname: ', validators=[DataRequired('Please enter your surname.')])
    email = StringField('Your email: ', validators=[DataRequired('Please enter your first name.'), Email()])
    password = PasswordField('Your password: ', validators=[DataRequired('Please enter your password.'),
                                                            Length(min=6, max=54,
                                                            message='Password must have 6 to 54 characters.')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Your email: ')
    password = PasswordField('Your password: ')
    submit = SubmitField('Log In')


class EditForm(FlaskForm):
    password = PasswordField('Confirm password: ', validators=[DataRequired('Please enter your first name.')])
    name = StringField('Your name: ', validators=[DataRequired('Please enter your first name.')])
    surname = StringField('Your surname: ', validators=[DataRequired('Please enter your first name.')])
    email = StringField('Your email: ', validators=[DataRequired('Please enter your first name.'), Email()])
    new_password = PasswordField('New password: ', validators=[DataRequired('Please enter your password.'),
                                                               Length(min=6, max=54,
                                                               message='Password must have 6 to 54 characters.')])
    submit = SubmitField('Update')
