from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, URLField, IntegerField, DateField
from wtforms.validators import DataRequired, URL, NumberRange

class ChiefForm(FlaskForm):
    rank = StringField('Rank', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired()])
    middle_name = StringField('Middle name')
    last_name = StringField('Last name', validators=[DataRequired()])
    decorations = StringField('Decoration', validators=[DataRequired()])
    date_took_office = DateField(' Date Took Office', format='%Y-%m-%d', validators=[DataRequired()])
    date_left_office = DateField('Date Left Office', format='%Y-%m-%d')
    dob = DateField('Date of birth', format='%Y-%m-%d')
    died = DateField('Date of death', format='%Y-%m-%d')
    bio = TextAreaField('Biography', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PictureForm(FlaskForm):
    url = URLField('URL', validators=[DataRequired(), URL()])
    title = StringField('Title', validators=[DataRequired()])
    chief_id = IntegerField('Chief ID', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Submit')

    