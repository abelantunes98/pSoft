# coding: utf-8

from threading import Thread
import socket
import sys
import os

porta = int(sys.argv[1] if(len(sys.argv) > 1) else 3102)
usuarios = {}
mensagens = []

def iniciaCliente(endereco, usuarios, mensagens):
    
    conexao = usuarios[endereco]
    with conexao as sk:
        
        mensagemSv = ""
        while mensagemSv != ":bye":
            mensagem = sk.recv(4096)
            mensagemSv = mensagem.decode('utf-8').split(os.linesep)[0]

            if (mensagemSv != ":bye"):
                # Adicionando a identificacao de quem está mandando a mensagem.
                saida = (str(endereco) + " " +  mensagemSv + os.linesep).encode('utf-8')
                mensagens.append((endereco ,saida))
           
            else:
                del usuarios[endereco]
                saida = str(endereco) + " saiu do grupo!" + os.linesep
                # Transforma em obj que pode ser enviado
                mensagens.append((endereco, saida.encode('utf-8')))
                
                
def receberClientes(usuarios, mensagens):
        
    while True:        
        # Escutando na porta
        s.listen()

        # Aceitando conexoes
        conexao, endereco = s.accept()
        usuarios[endereco] = conexao
        Thread(target=iniciaCliente, args=(endereco, usuarios, mensagens)).start() 


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Abrindo porta
    s.bind(('', porta))
    Thread(target=receberClientes, args=(usuarios, mensagens)).start()
    
    while True:

        while len (mensagens) > 0:
            for cli in usuarios.values():
                
                # Olha se o usuario nao eh o que mandou a mensagem
                if (mensagens[0][0] not in usuarios.keys()) or (cli != usuarios[mensagens[0][0]]):
                    cli.send(mensagens[0][1])
            mensagens.pop(0)
    

