from flask import Flask, render_template, url_for
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

allWork = [
            {
                'title':"Pie Chart.",
                'date':"2019-01-03",
                "content":"chart"
            },
    {
        'title': "Bar Chart",
        'date': "2019-01-01",
        "content": "chart"
    }
]

@app.route("/")
@app.route("/work")
def work():
    return render_template('work.html',allWork=allWork)

@app.route("/me")
def me():
    from me import meInfo
    meDetails = meInfo()

    return render_template('me.html',title="Me",meDetails=meDetails)

if __name__=='__main__':
    app.run(debug=True)


