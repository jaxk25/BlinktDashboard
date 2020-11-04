#!/usr/env python3

from flask import Flask, render_template
import blinkt
import os

app = Flask(__name__)

blinkt.set_clear_on_exit(True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False, port=int('80'), host='0.0.0.0')