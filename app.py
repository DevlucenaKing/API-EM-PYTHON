from flask import Flask, jsonify, request
app = Flask(__name__)
livros = [
   {
    'id': 1,
    'título': 'O Senhor dos Anéis - A Sociedade do Anel',
    'autor': 'J.R.R Tolkien'
   },
   {
    'id': 2,
    'título': 'Star Wars - DarkTimes',
    'autor': 'LucasFilm'
   },
   {
    'id': 3,
    'título': 'O homem elegante',
    'autor': 'Davi Lucena'
   },
]

# Consultar(todos)
@app.route('/livros' ,methods=['GET'])
def obter_livros():
    return jsonify(livros)
# Consultar(Id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
     for livro in livro:
        if livro.get('id') == id:
              return jsonify(livro)
# Editar
@app.route('livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
     livro_alterado = request.get_json()
     for indice,livro in enumerate(livros):
          if livro.get('id') == id:
            livros[indice].update(livro_alterado)

# Criar
@app.rount('livros/',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)
# Excluir
@app.route('livros/<int:id>',methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
          if livro.get('id') == id:
              del livros[indice]
              
              return jsonify(livros)
app.run(port=5000,host='localhost',debug=True)
