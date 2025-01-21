import socket
import signal
import sys

def stop_server(signal, frame):
    print('stop server')
    server_socket.close()
    sys.exit(0)

signal.signal(signal.SIGINT, stop_server) 

server_port = 1234
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', server_port)
server_socket.bind(server_address)
server_socket.listen(5)   

print(F"Server run on port {server_port}")

state = 0   

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Clinet connected: {client_address}")

    request = client_socket.recv(1024).decode()   
    print("Request accepted:\n", request)


    lines = request.split("\r\n")
    if len(lines) > 0:
        request_line = lines[0]  
        parts = request_line.split(" ")
        if len(parts) >= 2:
            method = parts[0]
            route = parts[1]

            if method == "POST" and route == "/on":
                state = 1
                response_body = "Light switched ON"
                print(response_body)
            elif method == "POST" and route == "/off":
                state = 0
                response_body = "Light switched OFF"
                print(response_body)
            else:
                response_body = "Route not found"

         
            if method == "OPTIONS":
                headers = "HTTP/1.1 200 OK\r\n"
                headers += "Access-Control-Allow-Origin: *\r\n"
                headers += "Access-Control-Allow-Methods: POST, GET, OPTIONS\r\n"
                headers += "Access-Control-Allow-Headers: Content-Type\r\n"
                headers += "Content-Type: text/html\r\n"
                response = ""
            else:
                headers = "HTTP/1.1 200 OK\r\n"
                headers += "Access-Control-Allow-Origin: *\r\n"
                headers += "Access-Control-Allow-Methods: POST, GET, OPTIONS\r\n"
                headers += "Content-Type: text/html\r\n"

                response = """<html>
                                <body>
                                   Ok
                                </body>
                            </html>"""

            client_socket.sendall((headers + "\r\n" + response).encode())
    client_socket.close()
