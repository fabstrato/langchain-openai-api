from flask import Flask, request, jsonify
from core.handler_chatbot import HandlerChatbot
from service.handler_modelo import HandlerModelo

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():

    retorno_req = request.get_json()
    prompt = """ """

    handlermodelo = HandlerModelo()
    handlerchatbot = HandlerChatbot(handlermodelo)

    output_ia = handlerchatbot.gerar_retorno_chatbot(retorno_req['body'], prompt)

    return jsonify(output_ia)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)