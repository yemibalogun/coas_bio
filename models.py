from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Chief(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=False)
    decorations = db.Column(db.String(225), nullable=False)
    date_took_office = db.Column(db.Date, nullable=False)
    date_left_office = db.Column(db.Date)
    dob = db.Column(db.Date, nullable=False)
    died = db.Column(db.Date, nullable=True)
    early_life = db.Column(db.Text, nullable=False)
    career = db.Column(db.Text, nullable=False)
    personal_life = db.Column(db.Text, nullable=True)
    death_and_commemoration = db.Column(db.Text, nullable=True)
    character_and_personality = db.Column(db.Text, nullable=True)
    influences_and_inspirations = db.Column(db.Text, nullable=True)
    quotes_and_anecdotes = db.Column(db.Text, nullable=True)
    references_and_sources = db.Column(db.Text, nullable=True)
    
    pictures = db.relationship('Picture', backref='chief', lazy=True)

    def __repr__(self):
        return f"Chief('{self.first_name}', '{self.middle_name}', '{self.last_name}', '{self.bio}')"

class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chief_id = db.Column(db.Integer, db.ForeignKey('chief.id'), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Pictures('{self.url}')"
    
