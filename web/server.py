from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/esprimo/<numero>')
def esprimo(numero):
    if(int(numero)>=1):
        for i in range(2, int(numero)):
            if (numero %i ==0):
                print(numero," no es numero primo")
            else:
                print(numero," es primo")
    else:
        print(numero," no es un numero primo")

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
