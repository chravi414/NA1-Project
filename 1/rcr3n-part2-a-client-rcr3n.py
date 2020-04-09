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
# To create socket object called 'client'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# To connect to the server
client.connect((IP_Address, port))
while True:
    message = str(
        input("Do you want to send  a message to the server?(y/n) : ")).lower()
    if(message == "y"):
        # To enter the message to be sent to server
        input_message = input("Enter your message : ")
        # To send the message to server
        client.send(input_message.encode())
    else:
        client.send("exit".encode())
        # To close the connection with server
        client.close()
        # Print statement
        print("connection closed with server")
        break
