# coding: utf-8

from threading import Thread
import socket
import sys

porta = int(sys.argv[1] if len(sys.argv) > 1 else 3100)
users = {}
mensagens = []

def iniciaCliente(endereco, users):
    
    conexao = users[endereco]
    with conexao as sk:
        while True:
            mensagem = sk.recv(4096)
            if mensagem == "bye":
                break

            mensagens.append(mensagem)



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Abrindo porta
    s.bind(('localhost', porta))
    # Escutando na porta
    s.listen()

    print ("Aguardando conexao na porta %s..." % porta)
    
    # Aceitando conexoes
    conexao, endereco = s.accept()
    users[endereco] = conexao
    Thread(target=iniciaCliente, args=(endereco, users)).start()


while True:
    while len(mensagens) > 0:
        for cli in users.values():
            cli.sendall(mensagens[0])

        mensagens.pop(0)
                



        
    

