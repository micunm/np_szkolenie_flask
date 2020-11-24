from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>/')
def hello_from_kwargs(name):
    return f'<h1>Hello string, {name}!</h1>'

@app.route('/user/<int:number>/')
def hello_number(number):
    return f'<h1>Hello string, {number}!</h1>'

@app.route('/user/<uuid:uuid_num>/')
def hello_uuid(uuid_num):
    return f'<h1>Hello uuid, {uuid_num}!</h1>'

@app.route('/user/<path:text>/<int:number>/')
def hello_both(text, number):
    return f'<h1>Hello both, {text}, {number}!</h1>'

### url converters
#Define functions:
#* hello_number(number: int):
#* hello_uuid(uuid):
#* hello_both(text, number):

#Visit:
#* http://127.0.0.1:5000/user/name/
#* http://127.0.0.1:5000/user/42/
#* http://127.0.0.1:5000/user/123e4567-e89b-12d3-a456-426614174000/
#* http://127.0.0.1:5000/user/he/man/42/  # make it work

if __name__ == '__main__':
    app.run()
