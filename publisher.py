import zmq, time
from constPS import * #-


context = zmq.Context()
socket = context.socket(zmq.PUB)  # Cria um socket de publicação

def send_message(topic, message):
    socket.send_multipart([bytes(topic, 'utf-8'), bytes(message, 'utf-8')])

# Conecta ao servidor
socket.connect("tcp://localhost:5555")

# Exemplos de envio de mensagens
send_message("user123", "Olá, usuário 123!")
send_message("topic1", "Esta é uma mensagem para o tópico 1.")
send_message("topic2", "Esta é uma mensagem para o tópico 2.")

