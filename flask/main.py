from flask import Flask, redirect, render_template, request
from pessoa import Pessoa

app = Flask(__name__)

pessoa1 = Pessoa(1, "Joao", "19", "1,80")
pessoa2 = Pessoa(2, "Thiago", "65", "1,60")
pessoa3 = Pessoa(3, "Marcio", "25", "1,70")
lista = [pessoa1, pessoa2, pessoa3]


@app.route("/")
def index():
    return render_template("index.html", titulo="Página inicial", pessoas=lista, qtdaRegistros=len(lista))


@app.route("/novo")
def novo():
    if len(lista) == 0:
        novoId = 0
    else:
        novoId = lista[-1].id + 1

    pessoa = Pessoa(novoId, "", "", "")
    return render_template("novo.html", titulo="Página de cadastro", pessoa=pessoa)


@app.route("/criar", methods=['POST'])
def criar():
    id = request.form['id']
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    lista.append(Pessoa(
        id,
        nome,
        idade,
        altura
    ))
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
