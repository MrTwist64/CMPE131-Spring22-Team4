from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password1')])
    securityQuestion = StringField('SecurityQuestion', validators=[DataRequired()])
    securityQuestionAnswer = PasswordField('SecurityQuestionAnswer', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me', validators=[DataRequired()])
    submit = SubmitField('Login')


class forgotPassForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Confirm')


class changePassForm(FlaskForm):
    securityQuestionAnswer = PasswordField('SecurityQuestionAnswer', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Confirm')


class updateForm(FlaskForm):
    firstname = StringField('firstname')
    lastname = StringField('lastname')
    username = StringField('username')
    email = StringField('Email', validators=[Email()])
    password1 = PasswordField('Password')
    password2 = PasswordField('Confirm Password', validators=[EqualTo('password1')])
    securityQuestion = StringField('SecurityQuestion')
    securityQuestionAnswer = PasswordField('SecurityQuestionAnswer')
    submit = SubmitField('Submit')
