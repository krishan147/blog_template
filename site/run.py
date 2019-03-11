from flask import Flask, render_template, url_for
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

    return render_template('me.html',title="Me",meDetails=meDetails,form=form)

if __name__=='__main__':
    app.run(debug=True)


