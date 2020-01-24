# app.py
from flask import Flask

app = Flask(__name__)

# setup a route
@app.route("/") 
# defines a method for this route
def hello(): 
    return "Test thing. Please ignore." 

if __name__ == "__main__":
    app.run()