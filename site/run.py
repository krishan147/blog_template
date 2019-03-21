from flask import Flask, render_template, url_for, flash, redirect, request
from flask_caching import Cache
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
    from me import message
    form = message()

    if request.method == 'POST':
        if form.validate_on_submit():
            # flash(f'Thank you {form.name.data}.','success')
            flash(f'Thank you','success')
            return redirect(url_for('work'))
    return render_template('me.html',title="Me",meDetails=meDetails,form=form)

if __name__=='__main__':
    app.run(debug=True)