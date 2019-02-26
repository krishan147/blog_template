from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "home"

@app.route("/contact")
def contact():
    return "contact"


@app.route("/work")
def work():
    return "work"

if __name__=='__main__':
    app.run(debug=True)