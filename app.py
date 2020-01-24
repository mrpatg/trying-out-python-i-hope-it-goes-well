# app.py
import farts
from flask import Flask
from flask import render_template


app = Flask(__name__)

# setup a route
@app.route("/") 
# defines a method for this route
def hello(): 
    return "Test thing. Please ignore." 

@app.route("/fart/on/<name>")
def jesuschrist(name=None):
    return render_template('name.html', name=name)

# second route
@app.route("/fart") 
# going to try to use other file's function
def whateverthefuck():
    return farts.raspberry()

if __name__ == "__main__":
    # run w/ debug on to reflect code changes and not have to restart server
    app.run(debug=True)