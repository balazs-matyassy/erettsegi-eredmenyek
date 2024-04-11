from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('hello_world.html', message='Érettségi eredmények |2024|')


@app.route('/akos')
def akos():
    return render_template('eredmenyek.html', name='Ákos', results=[5, 5, 5, 5, 5])


@app.route('/balazs')  # Balázs
def balazs():
    return render_template('eredmenyek.html', name='Balázs', results=[4, 5, 4, 5, 4])


if __name__ == '__main__':
    app.run()
