from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, EmailField
from wtforms.validators import DataRequired, Email


# pip install email-validator

class SignUpForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', default=18)
    gender = SelectField('Пол', choices=[("М", "Мужской"), ("Ж", "Женский")])
