from flask import Flask, render_template, url_for
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

posts = [
            {
                'author':"dog",
                'title':"cat",
                "content":"dog"
            },
    {
        'author': "dogg",
        'title': "horse",
        "content": "ddog"
    }
]

@app.route("/")
@app.route("/work")
def work():
    return render_template('work.html',posts=posts)

@app.route("/me")
def me():
    from me import meInfo
    parsed = meInfo()

    name =  parsed["name"]
    job =  parsed["job"]
    contact =  parsed["contact"]

    return render_template('me.html',title="Abouto",parsed=parsed)

if __name__=='__main__':
    app.run(debug=True)


