from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.csrf import CSRFProtect

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('Poster', validators=[
            FileRequired(),
            FileAllowed(['jpg', 'png'], 'Images only!')
        ])

    
