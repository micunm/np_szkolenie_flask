from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    user_info = {
        'name': 'Mike',
        'age': 42,
    }
    return render_template('index.html', user_info=user_info)


@app.route('/user/<name>/<int:amount>/')
def hello_from_kwargs(name, amount):
    return render_template('hello.html', name=name, amount=amount)
    #return f'<h1>Hello string, {name} ({amount})!</h1>'


if __name__ == '__main__':
    app.run()
