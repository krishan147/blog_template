import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
from wtforms.widgets import TextArea

def meInfo():
    workDets = json.load(open('me.json')) # change to add_your_about_info_here.json
    return workDets
# Message
class messages(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=300)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=1, max=1000)], widget=TextArea())
    submit = SubmitField('Send')

# Need to create form callback