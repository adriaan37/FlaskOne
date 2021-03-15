from flask import Flask, render_template

app = Flask(__name__)

email1="info@thebestone.com"
names = ["Andy", "Ben", "Charlie", "Devon", "Errol", "Frans", "Greg"]

@app.route('/')
def home():
    return render_template('home.html', email=email1)

@app.route('/about')
def about():
    return  render_template('about.html', nameslist=names)