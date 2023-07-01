import zmq
from constPS import * #-

context = zmq.Context()
socket = context.socket(zmq.SUB)  

def subscribe(topic):
    socket.setsockopt_string(zmq.SUBSCRIBE, topic)

# Conecta ao servidor
socket.connect("tcp://localhost:5555")

# Exemplos de assinatura de tópicos
subscribe("user123")  
subscribe("topic1") 

# Recebe e imprime as mensagens por um determinado número de iterações
for i in range(5):
    topic, message = socket.recv_multipart()
    print(f"Tópico: {topic.decode('utf-8')}\nMensagem: {message.decode('utf-8')}\n")

