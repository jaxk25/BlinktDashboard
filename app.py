#!/usr/env python3

# Import modules
from flask import Flask, render_template # Used to run webapp
import blinkt # Used to drive Blinkt pHat

# Function to change colour of Blinkt pHat
def changeColour(r,g,b):
    blinkt.set_all(r,g,b)
    blinkt.show()

app = Flask(__name__) # Define flask app

blinkt.set_clear_on_exit(True) # Tell the Blinkt module to clear any LEDs on exit

# Function to show index page
@app.route('/')
def index():
    return render_template('index.html')

# Function to recieve hexadecimal input and change Blinkt LED colour
@app.route('/<val>')
def change(val):
    val = str(val) # Convert to string
    h1,h2,h3,h4,h5,h6 = val[0],val[1],val[2],val[3],val[4],val[5] # Split the string
    hr,hg,hb = h1+h2,h3+h4,h5+h6 # Convert to 3 individual hex values
    r,g,b = int(hr, 16),int(hg, 16),int(hb, 16) # Convert to three denary values
    changeColour(r,g,b) # Call changeColour with three denary values
    return render_template('change.html') # Redirect to change.html

# Function to clear all LEDs on the Blinkt pHat
@app.route('/clear')
def clear():
    changeColour(0,0,0) # Call changeColour with three denary values
    return render_template('change.html') # Redirect to change.html

# Start program
if __name__ == "__main__": # Check if running as module or standalone
    app.run(debug=False, port=int('80'), host='0.0.0.0') # if running as a standalone app, start the flask webapp