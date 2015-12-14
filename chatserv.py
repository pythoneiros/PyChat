#-*- coding:utf-8 -*-

# --------------------------------------
# ChatServ
# Chat para intranet
# https://github.com/pythoneiros/ChatServ
# Licença MIT
# --------------------------------------

# Servidor de Históricos
servidor_chat = "chat"

# Arquivo da conversa
arquivo_chat = "historic-1.html"

# Conversa
caminho_chat = servidor_chat+'/'+arquivo_chat

# Comandos para sair
comandos_sair = ['#sair','#exit','#close',"#exit","#quit"]

# Entrada do nome
nomecompleto = raw_input('Digite seu nome: ').capitalize()

# Cor do usuário
from random import randrange
cor = str(randrange(0, 8))

# Código do batepapo
entrou = open(caminho_chat,'a')
entrou.write('\n<p><span  class="aviso"><strong>'+nomecompleto+'</strong> entrou no chat </span></p> \n\n')
entrou.close()

while True:
  with open(caminho_chat,'a') as chat:

    texto = raw_input('Você: ')

    while not texto:
      print '\n Ei.. digite algo! \n'
      texto = raw_input('Você: ')

    if texto in comandos_sair:
      chat.write('\n<p><span  class="aviso"><strong>'+nomecompleto+'</strong> saiu do chat</span></p> \n')
      print '\n Você saiu do chat, sua conversa foi salva em: '+caminho_chat+' \n'
      break
    else:
      chat.write('<p><span class="cor'+cor+'">'+nomecompleto+' disse:</span> '+texto+'<p>\n')


