from flask import Flask, render_template, request, redirect, url_for
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



@app.get("/<int:post_id>/edit")
def edit():
    return render_template("edit.html")

@app.post("/<int:post_id>/edit")
def editpost():
    with Session() as session:
        pizzaname = request.form.get("pizzaname")
        description = request.form.get("description")
        price = request.form.get("price")
        session.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?", (pizzaname, description, price))
        session.commit()
        session.close()
        return redirect(url_for("index"))



@app.post("/<int:post_id>/delete")
def delete(post_id):
    with Session() as session:
        # session.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        session.delete(post_id)
        session.commit()
        session.close()
        return redirect(url_for("index"))


if __name__ == '__main__':
    create_db()
    app.run(debug=True, port=40000)
