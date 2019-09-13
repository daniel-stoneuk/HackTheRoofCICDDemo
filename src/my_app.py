from flask import Flask,redirect,render_template

app = Flask(__name__)

@app.route('/')
def index():
            return render_template("index.html", message="Hello World!")
@app.route('/hack')
def hack_redirect():
            return redirect ("https://www.linkedin.com/in/derekslovin")
@app.route('/chalupabatman')
def chalupabatman_redirect():
            return redirect ("https://www.instagram.com/chalupabatman_the_bulldog/?hl=en")
