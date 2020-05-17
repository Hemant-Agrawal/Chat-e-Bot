import socket
import sys
import time


# creating Socket
def create_socket():
    try:
        global host
        global s
        global port
        host = ""
        port = 8099
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation error :  " + str(msg))


# Binding socket
def bind_socket():
    try:
        global host
        global s
        global port
        s.bind((host, port))
        s.listen(5)
        print("Binded to PORT ", port)
    except socket.error as msg:
        print("Socket Binding error :  " + str(msg) + "\n\nRetrying......")
        bind_socket()


# Establishing connection with a client
def socket_accept():
    global connection
    connection, address = s.accept()
    print("Connected to the server at IP " + str(address[0]) + " on Port " + str(address[1]))
    while True:
        send_commands()
    connection.close()


# Sending Commands

def send_commands():
    client_response = str(connection.recv(1024), "utf-8")
    print("client >", client_response)
    cmd = input("server >")
    connection.send(str.encode(cmd))


def Connection():
    create_socket()
    bind_socket()
    socket_accept()


Connection()
