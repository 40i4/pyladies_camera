from flask import Flask
import piggyphoto


app = Flask(__name__)


@app.route('/')
def hello_world():
    C = piggyphoto.camera()
    print(C.abilities)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
