from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
import secrets
secret = secrets.token_hex(16)

app = Flask(__name__)
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
    from me import meInfo
    meDetails = meInfo()
    from me import messages
    forms = messages()

    form_submission_list = []
    for key, value in request.form.items():
        form_submission_list.append(value)

    print (form_submission_list)




    if forms.validate_on_submit():
        flash(f'Thank you {forms.name.data}.','success')
        return redirect(url_for('work'))

    return render_template('me.html',title="Me",meDetails=meDetails,form=forms)


def __repr__(self):
    that =  f"User('{self.name}', '{self.email}','{self.message}')"
    print (that)
    return that

if __name__=='__main__':
    app.run(debug=True)