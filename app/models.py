# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import date

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    poster = db.Column(db.String(80))
    created_at = db.Column(db.Date)

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster

        today = date.today()
        created_at = today.strftime('%Y-%m-%d')

        self.created_at = created_at


    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Movie: %r>' % (self.title)