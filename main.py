from flask import Flask
from class_letter import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"

@app.route("/<name>")
def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)