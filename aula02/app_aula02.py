from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Rota principal será chamada quando digitar http://localhost:5000 no Browser
@app.route('/')
def index():
    dh = datetime.now()
    saida_dh = dh.isoformat(" ", timespec='seconds')
    hora = dh.hour
    cumprimento = "Bom dia"
    if hora > 11 and hora < 19:
        cumprimento = "Boa tarde"
    elif hora > 18 and hora < 24:
        cumprimento = "Boa noite"

    return render_template('index.html', data_hora=saida_dh, cumprimento=cumprimento)

# Rota para mostrar a tabuada de um número passado via URL: http://localhost:5000/tabuada?numero=7
@app.route('/tabuada/<numero>')
def tabuada(numero):
   if numero.isdigit() == False:
       return "Erro: Informe um número na URL!"
   n = int(numero)
   dados = []
   for contar in range(1, 11):
       dados.append([n, contar, n * contar])
   return render_template('tabuada.html', numero=numero, dados=dados)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/imprimir/<nome>')
def nome(nome):
    char = len(nome)
    return render_template('imprimir.html', nome=nome, char=char)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/fatorial/<numero>')
def fatorial(numero):
    if numero.isdigit() == False:
        return "Informe um numero na URL"
    n = int(numero)
    fat = ""
    result = 1
    for contador in range(1, n + 1):
        result *= contador
        fat += str(contador) + "x"

    fat = fat[0:len(fat) - 1] + " = " + str(result)
    return render_template('fatorial.html', numero=numero, fat=fat)

if __name__ == '__main__':
    app.run(debug=True)