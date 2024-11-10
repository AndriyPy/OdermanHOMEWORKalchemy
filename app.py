from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

app.get('/login/')


if __name__ == '__main__':
    app.run(debug=True, port=2020)