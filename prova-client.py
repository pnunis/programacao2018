import socket
HOST = socket.gethostbyname('localhost')
PORT = 22222


tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_client_socket.connect((HOST,PORT))
message = "Vai da certo!"
byte_msg = message.encode('utf-8')
tcp_client_socket.send(byte_msg)
data = tcp_client_socket.recv(1024)
tcp_client_socket.close
print("MSG recebido:", repr(data))