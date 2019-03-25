# coding: utf-8

import socket
import sys

porta = int(sys.argv[1] if len(sys.argv) > 1 else 3100)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Abrindo porta
    s.bind(('', porta))
    # Escutando na porta
    s.listen()

    print ("Aguardando conexao na porta %s..." % porta)
    
    # Aceitando conexoes
    conexao, endereco = s.accept()

    # Depois de conectado
    with conexao:
        print ("Conexao estabelecida de %s:%s..." % endereco)
        mensagem = "EchoCaps"

        # Para ao receber uma mensagem vazia
        while (mensagem != '\\n' and mensagem):
            print ("Aguardando mensagem de %s:%s" % endereco)
            mensagem = conexao.recv(4096)
            print("Mensagem: %s" % mensagem)
            # Devolvendo mensagem com uppercase
            conexao.sendall(mensagem.upper())
        
        conexao.close()


        
    

