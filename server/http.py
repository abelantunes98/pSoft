# coding: utf-8

# Abel Antunes de Lima Neto

import socket, sys, os

# Pegar ip publico
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('google.com', 80))
ipPublico = sk.getsockname()[0]

print ('IP público: %s' % ipPublico)

# Pegar ip local
ipLocal =  socket.gethostbyname(socket.gethostname())

print ('IP local do Server: %s' % ipLocal)

porta = int(sys.argv[1] if len(sys.argv) > 1 else 9090)

# Iniciando Server
sk = socket.socket()
sk.bind(('', porta))

sk.listen(10)
print ('Aguardando conexão com a porta %s' % str(porta))

request = {}
header = {}
body = {}

response = ''

def parse_request(mensagem):
    
    global respose

    protocol = "HTTP/1.1"
    code = 200
    status = "OK"
    mime_type = "text/html"
    charset = "charset=utf-8"
    corpo_response = "Este é o conteudo do recurso '/' neste servidor.<hr><h1>Directory Listing</h1><ul>"

    for p, _, files in os.walk(os.path.abspath(os.getcwd())):
        for file in files:
            caminho = os.path.join(p, file).split('/server/', 1)[-1]
            corpo_response += "<li><a href='" + caminho + "'>" + caminho + "</a></li>"

    corpo_response += "</ul>"

    try:
        mensagem = mensagem.decode().split("\r\n")

        # Verbo recurso e protocolo
        separado = mensagem[0].split()

        request["verbo"] = separado[0]
        request["recurso"] = separado[1]
        request["protocolo"] = separado[2]
        
        # Antes da ?
        myfile = request["recurso"].split("?")[0]
        
        try:
            
            # Ler arquivo em formato de bytes
            file = open(myfile, 'rb')
            corpo_response = file.read()
            corpo_response = corpo_response.decode()
            file.close()

            if (myfile.endwith(".jpg")):
                mime_type = "image/jpg"
            elif (myfile.endwith(".css")):
                mime_type = "text/css"
            elif (myfile.endwith(".html")):
                mime_type = "text/html"
            else:
                mime_type = "text/plain"

        except:
            code = 404
            status = "Not Found"
            corpo_response = "<html><body><center><h3> Error 404: Página não encontrada</h3><p>Python HTTP Server</p></center></body></html>"

        if (request["verbo"] != "GET"):
            code = 405
            status = "Method Not Allowed"
            corpo_response = "<html><body><center><h3>Error 405: Método Não suportado</h3><p>Python HTTP Server</p></center></body></html>"
        
        # Headers
        for i in range(1, len(mensagem)-1):
            if (mensagem[i]):
                # Encontra o primeiro :
                dp = mensagem[i].find(":")
                chave = mensagem[i][:dp]
                # Retira espacos no inicio e no final
                valor =  mensagem[i][dp+2:].strip()
                
                header[chave] = valor

        # Corpo
        corpo["corpo"] = mensagem[-2]
        
        # Retorna a mensagem ou nada
        response = ("%s %s %s \nContent-Type: %s;%s\nStatus: %s %s\n\n%s\n" % (protocolo, code, status, mime_type, charset, code, status, corpo_response)).encode('utf-8')

    except :
        print ("Erro ao passar seu pedido!")



while True:

    conexao, endereco = sk.accept()
    print ("Conectado com %s pela porta %s" % endereco)

    mensagem = conexao.recv(4096)
    parse_request(mensagem)
    conexao.send(response.encode('utf-8'))
    conexao.close()

s.close()


