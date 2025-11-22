from flask import Flask, render_template, request
from password_generator import generate_password

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    password = None
    if request.method == 'POST':
        letters = int(request.form['letters'])
        symbols = int(request.form['symbols'])
        numbers = int(request.form['numbers'])

        password = generate_password(letters, symbols, numbers)

    return render_template('home.html', password=password)


if __name__ == "__main__":
    app.run(debug=True)
