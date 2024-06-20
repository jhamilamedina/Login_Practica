from flask import Flask
from flask import render_template, request, redirect, url_for
from storage.storage import Storage

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/validate", methods=['POST'])
def validate():
    cnn = Storage()

    data = request.get_json()
    email = data['email']
    password = data['password']

    print(f'se recive {email} y {password}')

    cnn.connect()
    records = cnn.read()

    for r in records:
        if r[1] == email:
            if r[2] == password:
                print('Ingreso autorizado')
                return redirect(url_for('register'))
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
