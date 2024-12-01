from flask import Flask, render_template, request, redirect
from models import Session, Event, create_db
import requests


app = Flask(__name__)


api_key = "8cd4a140103c344ce454e7da889d1ced"




def get_weather(city):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
    data = r.json()
    weather_data = {
        "temp":data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "pressure":data["main"]["pressure"]


    }
    p = data["main"]
    print(p)

    return weather_data




@app.get('/')
def index():
    city = request.args.get('city')
    weather = get_weather(city)
    return render_template('index.html', weather=weather, city=city)




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




@app.get('/menu')
def menu():
    with Session() as session:
        data = session.query(Event).all()
    return render_template("menu.html", data=data)


if __name__ == '__main__':
    create_db()
    app.run(debug=True, port=40000)
