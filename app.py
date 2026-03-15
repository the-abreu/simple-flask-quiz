from flask import Flask, render_template
import random

app = Flask(__name__)

# Flashcards simples em memória
FLASHCARDS = [
    {"q": "O que é um algoritmo?", "a": "Uma sequência de passos ou instruções usadas para resolver um problema ou realizar uma tarefa."},
    {"q": "O que é uma variável?", "a": "Um espaço para armazenar valores (como números ou textos)."},
    {"q": "O que é uma função?", "a": "Um bloco de código que realiza uma tarefa e pode receber/retornar valores."},
    {"q": "O que é um loop?", "a": "Uma estrutura que repete ações várias vezes."},
    {"q": "O que é um comentário?", "a": "Texto no código para explicar algo, o interpretador ignora."},
]

@app.route("/")
def index():
    card = random.choice(FLASHCARDS)
    return render_template("index.html", card=card)

if __name__ == "__main__":
    app.run(debug=True)