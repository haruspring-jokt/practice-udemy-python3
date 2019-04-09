from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world'


if __name__ == '__main__':
    # 0.0.0.0 -> localhost:5000
    app.run(host='0.0.0.0', port=5000)
