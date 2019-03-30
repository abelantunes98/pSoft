# coding: utf-8

# Abel Antunes de Lima Neto - Matricula 117210287

from threading import Thread
import socket
import sys
import os

porta = int(sys.argv[1] if(len(sys.argv) > 1) else 3101)
usuarios = {}
mensagens = []

# Thread individual de cada cliente, passa à escutar o envio de mensagens e
# encaminhar para uma estrutura de dados do server
def iniciaCliente(endereco, usuarios, mensagens):
    
    conexao = usuarios[endereco]
    with conexao as sk:
        
        mensagemSv = ""
        while mensagemSv != ":bye":
            mensagem = sk.recv(4096)
            mensagemSv = mensagem.decode('utf-8').split(os.linesep)[0]

            if (mensagemSv != ":bye"):
                # Adicionando a identificacao de quem está mandando a mensagem.
                # Por descriicao, o indentificador é apenas o ip e a porta que se conectou
                saida = (str(endereco) + " " +  mensagemSv + os.linesep).encode('utf-8')
                mensagens.append((endereco ,saida))
           
            else:
                del usuarios[endereco]
                saida = str(endereco) + " saiu do grupo!" + os.linesep
                # Transforma em obj que pode ser enviado
                mensagens.append((endereco, saida.encode('utf-8')))
                

# Thread responsavel por receber novos clientes
def receberClientes(usuarios, mensagens):
        
    while True:        
        # Escutando na porta
        s.listen()
        print('Aguardando conexao na porta: %i' % porta)

        # Aceitando conexoes
        conexao, endereco = s.accept()
        usuarios[endereco] = conexao

        # Cria thread para cada cliente
        Thread(target=iniciaCliente, args=(endereco, usuarios, mensagens)).start() 


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   
    # Verificando IP externo
    s.connect(('google.com', 80))
    ipPublico = s.getsockname()[0]
    ipLocal = socket.gethostbyname(socket.gethostname())
    print ('IP público: %s' % ipPublico)
    print ('IP local: %s' % ipLocal)
    
    s = socket.socket()
    
    # Abrindo porta
    s.bind(('', porta))
   
    Thread(target=receberClientes, args=(usuarios, mensagens)).start()
    
    # Loop que verifica a entrada de novas mensagens, encaminha para os clientes e
    # às apaga por ordem de chegada
    while True:

        while len (mensagens) > 0:
            for cli in usuarios.values():
                
                # Olha se o usuario nao eh o que mandou a mensagem
                if (mensagens[0][0] not in usuarios.keys()) or (cli != usuarios[mensagens[0][0]]):
                    cli.send(mensagens[0][1])
            mensagens.pop(0)
    

