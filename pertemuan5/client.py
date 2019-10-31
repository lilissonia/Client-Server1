import socket


def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()     #instantiate
    client_socket.connect((host, port))     #connect to the server


    message = input(" -> ")     #take input

    while message.lower().strip() != 'byte'
        client_socket.send(message.encode())    #send message
        data = client_socket.recv(1024).decode()    #receive respon


        print('Received from server: ' + data)  #show in terminal

        message = input(' -> ')     #again take input

    client_socket.close()   #close the connection

