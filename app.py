from flask import Flask, render_template
import names

app = Flask(__name__)

#Generate random names
def GenerateNames(numberofnames):
    nlist = []
    for i in range(numberofnames):
        nlist.append(names.get_full_name())

    return nlist

namelist = GenerateNames(50)

#Homepage
@app.route('/')
def home():
    return render_template('home.html', namelist=namelist)