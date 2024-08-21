import socket
import os

WORKING_DIR = os.getcwd()

server = socket.socket()
server.bind(('', 80))

server.listen(1)

while True:
    conn, addr = server.accept()
    print(addr)
    request = conn.recv(10240).decode().split('\n')
    #print(request)
    method, url, protocol = request[0].split()
    url = os.path.join(WORKING_DIR, url[1:])
    print(url)
    
    code = "404 Not Found"
    body = ''

    if os.path.isdir(url):
        url = os.path.join(url, "index.htm")

    if os.path.isfile(url):
        code = "200 OK"
        body = open(url, 'r').read()

    responce = f"HTTP/1.1 {code}"
    responce += "Server: my_test_server 0.1"
    responce += "\n\n"
    responce += body

    conn.send(responce.encode())
    conn.close()
    print("Connection closed\n")
    