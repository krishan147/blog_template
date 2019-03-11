import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

def meInfo():
    workDets = json.load(open('me.json')) # change to add_your_about_info_here.json
    return workDets
# Message
class message(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=300)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = StringField('Message', validators=[DataRequired(), Length(min=1, max=1000)])
    submit = SubmitField('Send')