from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Érettségi eredmények |2024|'

@app.route('/akos')
def akos(): 
    return 'Ákos'


@app.route('/balazs')
def balazs():
    return 'Balázs'


if __name__ == '__main__':
    app.run()
