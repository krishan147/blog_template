from flask import Flask, render_template, url_for
app = Flask(__name__)

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

@app.route("/about")
def about():
    return render_template('about.html',title="Abouto",posts=posts)

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)