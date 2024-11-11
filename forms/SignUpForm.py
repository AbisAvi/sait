from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired


# pip install email-validator

class SignUpForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    gender = SelectField('Пол', choices=[("М", "Мужской"), ("Ж", "Женский")])
    rassa = SelectField('расса', choices=[("Ч", "Человек"), ("Э", "Эльф"), ("Пэ", "Полуэльф"), ("Т", "Тифлинг"), ("Д", "Дварф"), ("Г", "Гном"), ("П", "Полурослик"), ("Пр", "Полуорк"), ("Др", "Драконорождённый")])
