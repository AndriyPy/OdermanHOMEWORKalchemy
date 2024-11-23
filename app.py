from flask import Flask, render_template, request
from models import Session, Event, create_db


app = Flask(__name__)


@app.post('/admadd/')
def adm():
    with Session() as session:
        pizzaname = request.form.get("pizzaname")
        description = request.form.get("description")
        price = request.form.get("price")
        session.add(pizzaname,description,price)
        session.commit()

    return render_template('admin_add.html')

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/menu')
def menu():
    with Session() as session:
        data = session.query(Event).all()
    return render_template("menu.html", data=data)






if __name__ == '__main__':
    app.run(debug=True, port=40000)
    create_db()