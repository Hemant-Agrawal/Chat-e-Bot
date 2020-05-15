import socket

s = socket.socket()
host = "192.168.43.168"
port = 8099

s.connect((host, port))


def send_message(message):
    s.send(message.encode())
    data = s.recv(1024)
    response = data.decode("utf-8")
    print("Server >>", response)
    return response
