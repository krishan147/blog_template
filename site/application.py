from __future__ import print_function
from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from flask_caching import Cache
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import secrets
secret = secrets.token_hex(16)

application = app = Flask(__name__)
api = Api(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route("/")
@app.route("/work")
def work():
    from work import EachWork
    allWork = EachWork()
    return render_template('work.html',allWork=allWork)

app.config['SECRET_KEY'] = secret

@app.route("/me", methods=['GET', 'POST'])
def me():
    import json
    from me import meInfo
    meDetails = meInfo()
    from me import messages
    forms = messages()

    form_submission_list = []

    for key, value in request.form.items():
        form_submission_list.append(value)

    from gmail_send_only import run_email
    email_address = json.load(open('me.json'))['email']

    if len(form_submission_list) > 1:
        run_email.send_email(form_submission_list,email_address)
        form_submission_list = []
    else:
        pass

    if forms.validate_on_submit():
        flash(f'Thank you {forms.name.data}.','success')
        return redirect(url_for('work'))

    return render_template('me.html',title="Me",meDetails=meDetails,form=forms)

if __name__=='__main__':
    app.run(debug=True)