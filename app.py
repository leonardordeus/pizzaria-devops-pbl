from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(mensagem="Bem-vindo! Pizzaria Express a melhor pizza da cidade!")

@app.route('/status')
def status():
    # Código correto: retorna 200. Na aula, vamos quebrar isso mudando para 500.
    return jsonify(status="Ambiente Saudável"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
