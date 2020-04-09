# To import the socket module
import socket
# To get the Hostname of our Local system
Host_name = socket.gethostname()
# To print our Local Hostname
print(Host_name)
# To get the IP of our Local system based on our Hostname
IP_Address = socket.gethostbyname(Host_name)
# To print the IP Address of our Local Host
print(IP_Address)
# To initiate port number above 1024
port = 8080
# To create socket object called 'server'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# To bind the IP Address and Port number to the server
server.bind((IP_Address, port))
# To configure the number of clients the server can listen to simultaneously
server.listen(1)
print("Server waiting for connection from the client on port:", port)
# To accept new connection from the client
conn, address = server.accept()
# To print the address of the connected client to server
print("Connection established with: " + str(address))
while True:
    # To receive data stream from the connected client
    data = conn.recv(1024).decode()
    if(data == "exit"):
        # To print the data received from the client
        print("Message received from client: " + str(data))
        # To close the connection with server
        conn.close()
        print("connection closed with client")               # Print statement
        break
    else:
        print("Message received from client: " + str(data))  # Print statement
