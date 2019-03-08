def meInfo():
    import json
    from flask_wtf import FlaskForm
    from wtforms import StringField
    from wtforms.validators import DataRequired, Length, Email

    workDets = json.load(open('me.json')) # change to add_your_about_info_here.json

    # Form
    class RegistrationForm(FlaskForm):
        name = StringField('Name', validators=[DataRequired(),Length(min=1,max=250)])
        emailaddress = StringField('Email Address', validators=[DataRequired(),Email()])
        message = StringField('Message',Length(min=1,max=2500))



    return workDets