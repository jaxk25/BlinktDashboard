#!/usr/env python3

from flask import Flask, render_template
import blinkt
import os

def changeColour(r,g,b):
    blinkt.set_all(r,g,b)
    blinkt.show()

app = Flask(__name__)

blinkt.set_clear_on_exit(True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<val>')
def change(val):
    val = str(val)
    h1,h2,h3,h4,h5,h6 = val[0],val[1],val[2],val[3],val[4],val[5]
    hr,hg,hb = h1+h2,h3+h4,h5+h6
    r,g,b = int(hr, 16),int(hg, 16),int(hb, 16)
    changeColour(r,g,b)
    return render_template('change.html')

if __name__ == "__main__":
    app.run(debug=False, port=int('80'), host='0.0.0.0')