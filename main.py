from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/asdf/')
def index():
    # show request here
    user_info = {
        'name': 'Mike',
        'age': 42,
    }
    return render_template('index.html', user_info=user_info)


@app.route('/some_user/<name>/<amount>/')
def hello_from_kwargs(name, amount):
    amount = int(amount)
    return render_template('hello_from_kwargs.html', name=name, amount=amount)

#testowo:
app.add_url_rule('/', 'index', index)

if __name__ == '__main__':
    app.run()
