from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def create_table():
    sqlite_connection = sqlite3.connect('pizza.db')
    cursor = sqlite_connection.cursor()
    print('connection is successful')

    create_table_query = '''CREATE TABLE IF NOT EXISTS db_pizza_menu (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                description TEXT,
                                price REAL NOT NULL);'''
    cursor.execute(create_table_query)


    sqlite_connection.commit()
    print('table created')

    if sqlite_connection:
        sqlite_connection.close()
        print("З'єднання з SQL закрите")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.get('/admadd/')
def adm():
    return render_template('admin_add.html')


def dbsave(name, description, price):
    sqlite_connection = sqlite3.connect('pizza.db')
    cursor = sqlite_connection.cursor()
    print('connection is successful')

    sqlite_insert_with_param = """INSERT INTO db_pizza_menu 
                                  (name, description, price)
                                  VALUES(?, ?, ?)"""
    cursor.execute(sqlite_insert_with_param, name, description, price)
    sqlite_connection.commit()
    print('entry added')

    if (sqlite_connection):
        sqlite_connection.close()
        print("З'єднання з SQL закрите")



@app.post('/adm/')
def form_admin():
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']
    dbsave(name, description, price)
    return render_template('index.html')


if __name__ == '__main__':
    create_table()
    app.run(debug=True, port=2020)