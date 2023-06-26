from flask import Blueprint, render_template, request, jsonify, session, redirect
from .utils import ApiGPT

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def index_get():
    print(session)
    return render_template('home.html')

@views.route('/logout', methods=['GET'])
def index_logout():
    print(session.get('contexto'))
    session['contexto'] = False
    return redirect('/')

@views.route('/', methods=['POST'])
def index_post():
    mensagem = request.form.get('mensagem')

    if not session.get('contexto'):
        session['contexto'] = [
            {'role': 'system', 'content': 'Voce atuara como professor de uma universidade de historia, porem somente explicara sobre a segunda guerra mundial, qualquer pergunta nao relacionada a isso nao deve ser respondida, tente sempre responder com curiossidades sobre o fato perguntado.'},
            {'role': 'user', 'content': mensagem}
        ]
    else:
        session['contexto'].append({'role': 'user', 'content': mensagem})

    resposta_api = ApiGPT.chatGPT(mensagem, session['contexto'])
    session['contexto'].append({'role': 'system', 'content': resposta_api})

    if resposta_api is None:
        return jsonify({'status': 'Erro', 'erro': 'API retornando resposta invalida'}), 400

    return jsonify({'retornoAPi': resposta_api}), 200