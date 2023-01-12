import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2000))

x = 16740
y = 14850
flag = 0
bites = str([flag, x, y]).encode()

server.listen(30)
client_socket, adress = server.accept()


data = client_socket.recv(1024)

client_socket.send(bites)
