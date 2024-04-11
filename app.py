from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Érettségi eredmények |2024|'


@app.route('/akos')
def akos():
    return [5, 5, 5, 5, 5]


@app.route('/balazs')  # Balázs
def balazs():
    return [4, 5, 4, 5, 4]


if __name__ == '__main__':
    app.run()
