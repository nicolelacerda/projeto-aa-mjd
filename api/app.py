from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/apresentacao")
def apresentacao():
    return render_template("apresentacao.html")

@app.route("/materias")
def materias():
    return render_template("materias.html")

@app.route("/contato")
def contato():
    enviado = False
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        mensagem = request.form["mensagem"]
        enviado = True
        return render_template("contato.html", enviado=enviado, nome=nome, mensagem=mensagem)
        return render_template("contato.html", enviado=enviado)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
