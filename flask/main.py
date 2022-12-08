from flask import Flask, render_template
from pessoa import Pessoa

app = Flask(__name__)


@app.route("/")
def index():
    pessoa1 = Pessoa("Joao", "19", "1,80")
    pessoa2 = Pessoa("Thiago", "65", "1,60")
    pessoa3 = Pessoa("Marcio", "25", "1,70")
    pessoas = [pessoa1, pessoa2, pessoa3]
    return render_template("index.html", titulo="Página inicial", pessoas=pessoas)


if __name__ == "__main__":
    app.run(debug=True)
