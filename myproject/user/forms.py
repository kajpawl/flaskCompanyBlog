from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from myproject.models import User


class RegisterForm(FlaskForm):
    name = StringField('Your name: ', validators=[DataRequired('Please enter your first name.')])
    surname = StringField('Your surname: ', validators=[DataRequired('Please enter your surname.')])
    email = StringField('Your email: ', validators=[DataRequired('Please enter your first name.'), Email()])
    password = PasswordField('Your password: ', validators=[DataRequired('Please enter your password.'),
                                                            Length(min=6, max=54,
                                                            message='Password must have 6 to 54 characters.'),
                                                            EqualTo('pass_confirm', message='Passwords must match.')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email has been registered')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username has been registered')


class LoginForm(FlaskForm):
    email = StringField('Your email: ', validators=[DataRequired('Please enter your first name.'), Email()])
    password = PasswordField('Your password: ', validators=[DataRequired()])
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
