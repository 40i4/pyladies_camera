from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    to_jest_fajna_zmienna = "ala ma aids"
    return render_template("index.html", zmienna=to_jest_fajna_zmienna)


if __name__ == '__main__':
    app.run()
