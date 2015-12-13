#-*- coding:utf-8 -*-

import os
# --------------------------------------
# Informações
# --------------------------------------

arquivo_chat = os.path.join("chat","historic.txt")

comandos_sair = ['#sair','#exit','#close',"#exit","#quit"]

nomecompleto = raw_input('Digite seu nome: ').capitalize()

# --------------------------------------
# Código
# --------------------------------------

entrou = open(arquivo_chat,'a')
entrou.write('\n'+nomecompleto+' entrou no batepapo \n\n')
entrou.close()

while True:
  with open(arquivo_chat,'a') as chat:

    texto = raw_input('Você: ')

    while not texto:
      print '\n Ei.. digite algo! \n'
      texto = raw_input('Você: ')

    if texto in comandos_sair:
      chat.write('\n'+nomecompleto+' saiu do batepapo \n')
      print '\n Você saiu do batepapo. \n'
      break
    else:
      chat.write(nomecompleto+' disse: '+texto+'\n')


