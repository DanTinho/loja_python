from flask import Flask, render_template

app = Flask(__name__)

# Dados de exemplo para os produtos
produtos = [
    {"id": 1, "nome": "Vara de Pesca com Molinete 200m", "preco": 149.90, "imagem": "vara_de_pesca.jpg"},
    {"id": 2, "nome": "Linha de Pesca Dourado 100g 600 Metros", "preco": 49.90, "imagem": "linha.jpg"},
    {"id": 3, "nome": "Jogo de Anzol Black Chinu 10 unidades", "preco": 19.90, "imagem": "anzol.jpg"},
    {"id": 4, "nome": "Isca Artificial 12cm", "preco": 14.90, "imagem": "isca.jpg"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produtos')
def mostrar_produtos():
    return render_template('produtos.html', produtos=produtos)

@app.route('/produto/<int:produto_id>')
def produto_unico(produto_id):
    produto = next((p for p in produtos if p["id"] == produto_id), None)

    if produto is None:
        ConnectionAbortedError
    else:
        return render_template('produto_específico.html', produto=produto)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)