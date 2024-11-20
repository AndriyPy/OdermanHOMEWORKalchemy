from flask import Flask, render_template, request
from models import Session, Event


app = Flask(__name__)



@app.get('/')
def index():
    return render_template('index.html')


@app.get('/menu')
def menu():
    return render_template("menu.html")

@app.get('/admadd/')
def adm():
    return render_template('admin_add.html')




if __name__ == '__main__':
    app.run(debug=True, port=2020)