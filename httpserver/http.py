# coding: utf-8

# Abel Antunes de Lima Neto - Matricula 117210287

import socket, sys, os
from _thread import *

# Pegar ip publico
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('google.com', 80))
ipPublico = sk.getsockname()[0]

print ('IP público: %s' % ipPublico)

# Pegar ip local
ipLocal =  socket.gethostbyname(socket.gethostname())

print ('IP local do Server: %s' % ipLocal)

porta = int(sys.argv[1] if len(sys.argv) > 1 else 8090)

# Iniciando Server
sk = socket.socket()
sk.bind(('', porta))

sk.listen(10)
print ('Aguardando conexão com a porta %s' % str(porta))

# Dicionarios da pagina de saída
vrp = {}
header = {}
body = {}

response = ''

# Analisa o pedido do cliente e gera uma saida ou uma mensagem de erro, caso o request
# não seja compreendido
def parse_request(mensagem):
    
    global response
    
    # Valores default
    protocol = "HTTP/1.1"
    code = 200
    status = "OK"
    mime_type = "text/html"
    charset = "charset=utf-8"
    corpo_response = "Este é o conteudo do recurso '/' neste servidor.<hr><h1>Directory Listing</h1><ul>"
    
    try:

        # Separando o pedido
        mensagem = mensagem.decode().split("\r\n")
        # Verbo recurso e protocolo
        separado = mensagem[0].split()

        vrp["verbo"] = separado[0]
        vrp["recurso"] = separado[1]
        vrp["protocolo"] = separado[2]
        
        # O server só conhece o método GET, se for diferente, já retorna erro
        if (vrp["verbo"] != "GET"):
            code = 405
            status = "Method Not Allowed"
            corpo_response = "<html><body><center><h3>Error 405: Método Não suportado</h3><p>Python HTTP Server</p></center></body></html>"
        
        else:
            # Antes da ?
            myfile = vrp["recurso"].split("?")[0]
            
            # Se o request pedir a raiz do dir, é pego o nome dos arquivos guardados e gerado links
            if (myfile == '/'):
                # Pegando os nomes dos arquivos no diretório do server e gerando o body com seus
                # nomes
                for p, _, files in os.walk(os.path.abspath(os.getcwd())):
                    for file in files:
                        caminho = os.path.join(p, file).split('/httpserver/', 1)[-1]
                        corpo_response += "<li><a href='" + caminho + "'>" + caminho + "</a></li>"

                corpo_response += "</ul>"

            else:
            
                try:
                    
                    # Se for pedido um arquivo especifico, seu conteudo será o corpo do response
                    # Isso se o arquivo existir ralmente
                    myfile = myfile.lstrip('/')
                    # Ler arquivo em formato de bytes
                    file = open(myfile, 'rb')
                    corpo_response = file.read()
                    corpo_response = corpo_response.decode()
                
                    file.close()

                    if (myfile.strip(".") == 'jpg'):
                        mime_type = "image/jpg"
                    elif (myfile.strip(".") == 'css'):
                        mime_type = "text/css"
                    elif (myfile.strip(".") == 'html'):
                        mime_type = "text/html"
                    else:
                        mime_type = "text/plain"

                except:
                    code = 404
                    status = "Not Found"
                    corpo_response = "<html><body><center><h3> Error 404: Página não encontrada</h3><p>Python HTTP Server</p></center></body></html>" 
        
        # Guardando Headers no dict
        for i in range(1, len(mensagem)-1):
            if (mensagem[i]):
                # Encontra o primeiro :
                dp = mensagem[i].find(":")
                chave = mensagem[i][:dp]
                # Retira espacos no inicio e no final
                valor =  mensagem[i][dp+2:].strip()
                
                header[chave] = valor
       
        
        # Guardando o corpo no dict
        body["corpo"] = mensagem[-2]
        
        # Retorna a mensagem ou nada
        response = ("%s %i %s \nContent-Type: %s;%s\nStatus: %i %s\n\n%s\n" % (protocol, code, status, mime_type, charset, code, status, corpo_response)).encode()
        
    except :
        print ("Erro ao passar seu pedido!")



# Loop que aguarda novas conexoes e requests
while True:
    
    conexao, endereco = sk.accept()
    print ("Conectado com %s pela porta %s" % endereco)

    mensagem = conexao.recv(4096)
    parse_request(mensagem)
    conexao.send(response)
    conexao.close()

s.close()


