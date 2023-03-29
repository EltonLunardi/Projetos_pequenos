from twilio.rest import Client
from flask import Flask, request, redirect
import requests

# Configurações da sua conta Twilio e WhatsApp Business API
account_sid = 'AC67bdf1afbc0971ae6fa035cc8e250589'
auth_token = '92d1ec98bf58274a37e9ba3b43ae6874'
client = Client(account_sid, auth_token)
twilio_whatsapp_number = 'whatsapp:+14754451232'

app = Flask(__name__)


@app.route('/', methods=['POST'])
def receive_message():
    """
    Função que recebe as mensagens enviadas pelos usuários
    """
    # Obtém a mensagem recebida
    incoming_message = request.values.get('Body', '').lower()
    sender_number = request.values.get('From')

    # Lógica de gerenciamento de negócios aqui
    response = gerenciar_negocios(incoming_message)

    # Envia a resposta de volta para o usuário
    send_message(sender_number, response)

    return '', 200


def gerenciar_negocios(incoming_message):
    """
    Função que processa a mensagem recebida e retorna a resposta apropriada
    """
    # Lógica de gerenciamento de negócios aqui
    if 'pedido' in incoming_message:
        return 'Seu pedido será entregue em breve!'
    elif 'suporte' in incoming_message:
        return 'Entre em contato conosco pelo email suporte@meunegocio.com'
    else:
        return 'Obrigado por entrar em contato com a gente!'


def send_message(sender_number, message):
    """
    Função que envia a mensagem de volta para o usuário
    """
    client.messages.create(
        from_=twilio_whatsapp_number,
        body=message,
        to=sender_number
    )


if __name__ == '__main__':
    app.run()
