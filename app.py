from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Rafael',
        'lista_habilidades': ['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Ilmar',
        'lista_habilidades': ['Python', 'Django']
    }
]


@app.route("/dev/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da API"
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(desenvolvedores[id])
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})


@app.route("/dev", methods=['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'GET':
        return jsonify(desenvolvedores)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])


if __name__ == '__main__':
    app.run(debug=True)
