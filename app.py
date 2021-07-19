from flask import Flask

app = Flask(__name__)

host = '0.0.0.0'

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host=host)
