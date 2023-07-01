import zmq
from constPS import * #-

context = zmq.Context()
socket = context.socket(zmq.SUB)  # Cria um socket de assinatura

def subscribe(topic):
    socket.setsockopt_string(zmq.SUBSCRIBE, topic)

# Conecta ao servidor
socket.connect("tcp://localhost:5555")

# Exemplos de assinatura de tópicos
subscribe("user123")  # Assina as mensagens direcionadas ao usuário 123
subscribe("topic1")  # Assina as mensagens do tópico 1

# Recebe e imprime as mensagens por um determinado número de iterações
for i in range(5):
    topic, message = socket.recv_multipart()
    print(f"Tópico: {topic.decode('utf-8')}\nMensagem: {message.decode('utf-8')}\n")

