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
    return render_template("contato.html")

