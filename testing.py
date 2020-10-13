import os
import sys
import subprocess
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def home():
	return jsonify("This is a testing project.")


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/ip_addr")
def win_cmd():
    cmd1 = "ipconfig"
    output = subprocess.Popen( cmd1, stdout=subprocess.PIPE ).communicate()[0]
    return output

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')