
import socket, sys

s = socket.socket()

porta = int(sys.argv[1] if len(sys.argv) > 1 else 9091)

s.bind(('{}'.format(socket.gethostbyname(socket.gethostname())), porta))

s.listen(10)
print("Aguardando conexão com a porta {}".format(porta))

while True:
    msg = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<html><body>Hello World</body></html>\n".encode()
    sock, addr = s.accept()
    sock.send(msg);
    sock.close()
