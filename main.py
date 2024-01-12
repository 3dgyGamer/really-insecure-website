from flask import Flask, render_template, request, redirect
import os, io

app = Flask(__name__)


#keeping the passwords in code for now.
passwords = ['3mK8cB325C9vy9fKALUE']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/level1')
def level1():
    return render_template("level1.html")

@app.route('/level2')
def level2():
    pass




if __name__ == "__main__":
    app.run(debug=True)