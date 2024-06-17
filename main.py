from flask import Flask, render_template, url_for, flash, redirect
from config import Config
from models import Chief, db, Picture
from forms import ChiefForm, PictureForm
from datetime import datetime


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def truncate_bio(bio, lines=1):
    bio_lines = bio.split('\n')
    truncated = bio_lines[:lines]
    return '\n'.join(truncated) + ('...' if len(bio_lines) > lines else '')

def format_date(date):
    return date.strftime('%d %B %Y') if date else None

@app.route('/')
def home():
    chiefs = Chief.query.all()
    for chief in chiefs:
        chief.truncated_bio = truncate_bio(chief.bio)
        chief.formatted_date_took_office = format_date(chief.date_took_office)
        chief.formatted_date_left_office = format_date(chief.date_left_office)
    return render_template('index.html', chiefs=chiefs)

@app.route('/add_chief', methods=['GET', 'POST'])
def add_chief():
    chief_form = ChiefForm()
    if chief_form.validate_on_submit():
        rank = chief_form.rank.data
        first_name = chief_form.first_name.data
        middle_name = chief_form.middle_name.data
        last_name = chief_form.last_name.data
        decorations = chief_form.decorations.data
        date_took_office = chief_form.date_took_office.data
        date_left_office = chief_form.date_left_office.data
        dob = chief_form.dob.data
        died = chief_form.died.data
        bio = chief_form.bio.data

        chief = Chief(
            rank=rank,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            decorations=decorations,
            date_took_office=date_took_office,
            date_left_office=date_left_office,
            dob=dob,
            died=died,
            bio=bio
            )
        db.session.add(chief)
        db.session.commit()
        flash('Chief added successfully!')
        return redirect(url_for('home'))
    return render_template('add_chief.html', chief_form=chief_form)
    
@app.route('/add_picture', methods=['GET', 'POST'])
def add_picture():
    picture_form = PictureForm()
    if picture_form.validate_on_submit():
        url = picture_form.url.data
        title = picture_form.title.data
        chief_id = picture_form.chief_id.data
        picture = Picture(
            url=url,
            title=title,
            chief_id = chief_id
        )
        db.session.add(picture)
        db.session.commit()
        flash('Picture added successfully!')
        return redirect(url_for('home'))
    return render_template('add_picture.html', picture_form=picture_form)

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 