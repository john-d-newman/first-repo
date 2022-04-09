'''
This is the stuff about the webserver

something about pip3
install flask
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

def foo(name):
    print("hello" + name)


app.run(host="127.0.0.1", port=8080)