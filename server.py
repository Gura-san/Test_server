import socket

server = socket.socket()
server.bind(('', 80))

server.listen(1)

while True:
    conn, addr = server.accept()
    print(addr)
    request = conn.recv(10240).decode()
    print(request)

    responce = 'test'
    conn.send(responce.encode())
    conn.close()
    print("Connection closed\n")
    