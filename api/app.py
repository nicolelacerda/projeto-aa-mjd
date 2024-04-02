import requests
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/apresentacao")
def apresentacao():
    return render_template("apresentacao.html")

@app.route("/materias")
def materias():
    req_jota_melissa=requests.get("https://www.jota.info/autor/melissa-duartejota-info")
    conteudo_jota_melissa=req_jota_melissa.content
    html_jota_melissa=BeautifulSoup(conteudo_jota_melissa)
    noticias=html_jota_melissa.findAll('div',{'class':'jota-posts-list__body'})

    materias_melissa=[]
    for noticia in noticias:
        titulo=noticia.find('h3').text.strip()
        link=noticia.find('a').get('href')
        materias_melissa.append({"titulo": titulo, "link": link})
    print(materias_melissa)    
    return render_template("materias.html" , materias=materias_melissa)

@app.route("/contato")
def contato():
    enviado = False
    return render_template("contato.html")

@app.route("/enviar_contato" , methods=["POST" , "GET"])
def enviar_contato():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        mensagem = request.form["mensagem"]
        enviado = True
        print(mensagem)
        return "Deu certo"



if __name__ == '__main__':
    app.run(port=5000, debug=True)
