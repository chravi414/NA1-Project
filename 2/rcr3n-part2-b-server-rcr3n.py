import socket

HOST = ''
PORT = 4000


def connect():
    sock = socket.socket()
    server = sock.bind((HOST, PORT))
    sock.listen(1)
    print("Server is Listening...")
    conn, addr = sock.accept()
    return conn


def send_messages(c):
    while True:
        msg = str(c.recv(1024).decode())
        msg = msg.lower()
        if msg == "bye":
            print(msg)
            c.send(str.encode("Server connection is closed"))
            c.close()
            c = connect()
            send_messages(c)

            # break
        elif msg == "hello from client-ravi":
            print(msg)
            c.send(str.encode("Hello from Server"))
        else:
            print(msg)
            c.send(str.encode(msg))


def main():
    c = connect()
    send_messages(c)


if __name__ == '__main__':
    main()
