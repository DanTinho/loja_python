from flask import Flask, render_template

app = Flask(__name__)

# Dados de exemplo para os produtos
produtos = [
    {"id": 1, "nome": "Camiseta Básica", "preco": 49.90, "imagem": "camiseta.jpg"},
    {"id": 2, "nome": "Calça Jeans", "preco": 129.90, "imagem": "jeans.jpg"},
    {"id": 3, "nome": "Vestido Elegante", "preco": 199.90, "imagem": "vestido.jpg"},
    {"id": 4, "nome": "Jaqueta de Couro", "preco": 299.90, "imagem": "jaqueta.jpg"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produtos')
def mostrar_produtos():
    return render_template('produtos.html', produtos=produtos)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)