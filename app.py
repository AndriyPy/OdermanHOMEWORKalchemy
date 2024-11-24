from flask import Flask, render_template, request, redirect
from models import Session, Event, create_db

app = Flask(__name__)


@app.get('/admadd/')
def adm_get():
    return render_template('admin_add.html')



@app.post('/admadd/')
def adm():
    with Session() as session:

        pizzaname = request.form.get("pizzaname")
        description = request.form.get("description")
        price = request.form.get("price")
        new_event = Event(pizzaname=pizzaname, description=description, price=price)
        session.add(new_event)
        session.commit()
        return redirect("/menu")
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
    create_db()
    app.run(debug=True, port=40000)
