from flask import Flask,redirect,render_template,send_file
from google.cloud import storage
import tempfile
import random

app = Flask(__name__)

@app.route('/')
def index():
            return render_template("index.html", message="Hello World!!")
@app.route('/hack')
def hack_print():
            return render_template("index.html", message="Hack The Roof!")
@app.route('/chalupa/',defaults={'filename': 'a'})
@app.route('/chalupa/<filename>')
def chalupa_print_by_num(filename):
            client = storage.Client()
            bucket = client.get_bucket('chalupa-images')
            blob = bucket.get_blob(filename)
            if not blob:
               blobs = client.list_blobs(bucket)
               l_blobs = list(blobs)
               filename = l_blobs[random.randint(0,len(l_blobs))].name
               blob = bucket.get_blob(filename)         
            with tempfile.NamedTemporaryFile() as temp:
                        blob.download_to_filename(temp.name)
                        return send_file(temp.name, mimetype='image/jpg')
@app.route('/chalupabatman')
def chalupabatman_redirect():
            return redirect ("https://www.instagram.com/chalupabatman_the_bulldog/?hl=en")
