import socket


def server_program():
    #get the hostname
    host = socket.gethostname()
    port = 5000 #initiate port no above 1024


    server_socket = socket.socket() #get instance
    #look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port)) #bind host addres and port

    #configure how many client the server can listen simultanecusly
    server_socket.listen(2)
    conn, address = server_socket.accept() #accept new connection
    print("connection from : " + str(address))
    #
    while True:
        #receive data stream, it won't accept data packet greater
        data = conn.recv(1024).decode()
        if not data:
            #
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())

    conn.close()


server_program()
#if_name_=='__main_