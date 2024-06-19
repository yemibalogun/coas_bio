from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField, IntegerField, DateField
from wtforms.validators import DataRequired

class ChiefForm(FlaskForm):
    rank = StringField('Rank', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired()])
    middle_name = StringField('Middle name')
    last_name = StringField('Last name', validators=[DataRequired()])
    decorations = StringField('Decoration', validators=[DataRequired()])
    date_took_office = DateField(' Date Took Office', format='%Y-%m-%d', validators=[DataRequired()])
    date_left_office = DateField('Date Left Office', format='%Y-%m-%d')
    dob = DateField('Date of birth', format='%Y-%m-%d', validators=[DataRequired()])
    died = DateField('Date of death', format='%Y-%m-%d')
    early_life = TextAreaField('Early life', validators=[DataRequired()])
    career = TextAreaField('Career')
    personal_life = TextAreaField('Personal life')
    death_and_commemoration = TextAreaField('Death and commemoration')
    character_and_personality = TextAreaField('Character and personality')
    influences_and_inspirations = TextAreaField('Influences and inspirations')
    quotes_and_anecdotes = TextAreaField('Quotes and anecdotes')
    references_and_sources = TextAreaField('References and sources')
    submit = SubmitField('Submit')

class PictureForm(FlaskForm):
    chief_id = IntegerField('Chief ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    picture = FileField('Upload Picture', validators=[DataRequired()])
    submit = SubmitField('Upload Picture')

    