from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, Required,Length, Email, EqualTo
from app.models import User

class Login(FlaskForm):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Sign In')


class Registration(FlaskForm):
    username = StringField('Username', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    password_confirm = PasswordField('Confirm Password', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already exists')

    '''
    the method above issue database queries expecting there
    will be no results. In the event a result already exists,
    a validation error is triggered by raising ValidationError
    '''

class ResetPasswordRequest(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPassword(FlaskForm):
    password = PasswordField('Password', validators=[Required()])
    password2 = PasswordField(
        'Repeat Password', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
