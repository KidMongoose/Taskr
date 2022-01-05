# from flask_wtf import FlaskForm
# from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, email_validator
# from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FileField
# from models import *


# class LoginForm(FlaskForm):
#     email = StringField('E-mail', validators=[DataRequired(), Email()])
#     remember_me = BooleanField('Remember me')
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('login')

# class RegistrationForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     email  = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Register')
    
#     def validate_name(self, name):
#         user = User.query_filter_by(name=name.data).first()
#         if user is not None:
#             return ValidationError('Please use a different username.')

#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         if user is not None:
#             return ValidationError('Please use a different e-mail.')

  
# class ContactForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     telephone = StringField('Telephone', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     image = FileField()
#     category = StringField('Category', validators=[DataRequired()])
#     company = StringField('Company', validators=[DataRequired()])
#     contact_type = StringField('Contact Type', validators=[DataRequired()])
#     title = StringField('Title', validators=[DataRequired()])
#     notes = TextAreaField('Notes', validators=[DataRequired()])
#     save = SubmitField('Save')



# class TaskForm(FlaskForm):
#     title = StringField('Title', validators=[DataRequired()])
#     item_type = StringField('Item Type', validators=[DataRequired()])
#     priority = StringField('Priority', validators=[DataRequired()])
#     status = StringField('Status', validators=[DataRequired()]) 
#     category = StringField('Category', validators=[DataRequired()])
#     task_note = TextAreaField('Task', validators=[DataRequired()])
#     save = SubmitField('Save')
