"""This is the main flask app file"""
from random import randint, random
from flask import Flask, render_template
import names

app = Flask(__name__)

def generate_names(numberofnames):
    """Generate random names"""
    nlist = []
    for i in range(numberofnames):
        nlist.append(names.get_full_name())
        print(i)

    return nlist

namelist = generate_names(50)

@app.route('/')
def home():
    """Render Homepage"""
    return render_template('home.html', namelist=namelist)

def test_generate_names():
    """This is a test for generate_names"""
    namelist = generate_names(101)
    assert len(namelist) == 101

def test_generate_names_check_type():
    """This is a test for generate_names to check type"""
    namelist = generate_names(101)
    assert isinstance(namelist, list)

def test_generate_names_check_string():
    """This is a test to check if the names generated are strings"""
    namelist = generate_names(50)
    i = randint(1,50)
    assert isinstance(namelist[i], str)
    