from flask import Flask, render_template
import random

app = Flask(__name__)

flashcards = [
    {"question": "O que é uma variável?", "answer": "Um espaço para armazenar valores."},
    {"question": "O que é uma função?", "answer": "Um bloco de código reutilizável."},
    {"question": "O que é um loop?", "answer": "Estrutura que repete ações."}
]

@app.route("/")
def index():
    card = random.choice(flashcards)
    return render_template("index.html", card=card)

if __name__ == "__main__":
    app.run(debug=True)