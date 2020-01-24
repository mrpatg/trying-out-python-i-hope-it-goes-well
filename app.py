# app.py
from flask import Flask
from app import farts

app = Flask(__name__)


# setup a route
@app.route("/") 
# defines a method for this route
def hello(): 
    return "Test thing. Please ignore." 

# second route
@app.route("/fart") 
# going to try to use other file's function
farts.raspberry()

if __name__ == "__main__":
    # run w/ debug on to reflect code changes and not have to restart server
    app.run(debug=True)