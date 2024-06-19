from flask import Flask, render_template, url_for, flash, redirect, current_app
from config import Config
from werkzeug.utils import secure_filename
from PIL import Image
from models import Chief, db, Picture
from forms import ChiefForm, PictureForm
from datetime import datetime
import os
import secrets


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

def resize_image(image_path, output_size):
    """Resize the image to the specified output size."""
    with Image.open(image_path) as img:
        img.thumbnail(output_size)
        img.save(image_path)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/images', picture_fn)

    # Resize image
    output_size = (280, 280)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def truncated_early_life(early_life, word_limit=10):
    words = early_life.split()
    truncated = words[:word_limit]
    return ' '.join(truncated) + ('...' if len(words) > word_limit else '')

def format_date(date):
    return date.strftime('%d %B %Y') if date else None

@app.route('/')
def home():
    chiefs = Chief.query.all()
    for chief in chiefs:
        chief.truncated_early_life = truncated_early_life(chief.early_life)
        chief.formatted_date_took_office = format_date(chief.date_took_office)
        chief.formatted_date_left_office = format_date(chief.date_left_office)
    return render_template('index.html', chiefs=chiefs)

@app.route('/chief/<int:chief_id>')
def chief_profile(chief_id):
    chief = Chief.query.get_or_404(chief_id)
    chief.truncated_early_life = truncated_early_life(chief.early_life)
    chief.formatted_date_took_office = format_date(chief.date_took_office)
    chief.formatted_date_left_office = format_date(chief.date_left_office)
    
    return render_template('chief_profile.html', chief=chief, pictures=chief.pictures)

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
        early_life = chief_form.early_life.data
        career = chief_form.career.data
        personal_life = chief_form.personal_life.data
        death_and_commemoration = chief_form.death_and_commemoration.data
        character_and_personality = chief_form.character_and_personality.data
        influences_and_inspirations = chief_form.influences_and_inspirations.data
        quotes_and_anecdotes = chief_form.quotes_and_anecdotes.data
        references_and_sources = chief_form.references_and_sources.data

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
            early_life=early_life,
            career=career,
            personal_life=personal_life,
            death_and_commemoration=death_and_commemoration,
            character_and_personality=character_and_personality,
            influences_and_inspirations=influences_and_inspirations,
            quotes_and_anecdotes=quotes_and_anecdotes,
            references_and_sources=references_and_sources
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
        picture_file = save_picture(picture_form.picture.data)
        picture = Picture(
            chief_id=picture_form.chief_id.data, 
            title=picture_form.title.data, 
            url=picture_file
            )
        db.session.add(picture)
        db.session.commit()
        flash('Your picture has been uploaded!', 'success')
        return redirect(url_for('home'))
    return render_template('add_picture.html', picture_form=picture_form)

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 