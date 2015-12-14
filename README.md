# ChatServ
Chat para intranet desenvolvido em Python

***OBS:*** Baseado no algoritmo do [@marlysson](https://github.com/pythoneiros/Exercicios/blob/master/Exercicio-3/Marlysson/exercicio.py) ;)

### Como usar

Após o Download, execute o arquivo ```chatserv.py``` no terminal usando o seguinte comando:

    python chatserv.py


### Configurando
Todos os históricos são salvos por padrão na pasta ```/chat```, entretanto caso você queira conversar em grupo dentro de uma rede local copie a pasta em um servidor web dentro da sua rede, em seguida altere a variavel ```servidor_chat = "chat"``` para o endereço e caminho do servidor, exemplo:

    servidor_chat = "http://192.168.0.1/chat"


O nome do arquivo que irá salvar o histórico de sua conversa pode ser alterado na variavel ```arquivo_chat = "historic-1.html"```, também localizada dentro do arquivo ```chatserv.py```, exemplo:

    arquivo_chat = "conversa-equipe-x.html"


***OBS: O arquivo de histórico deve estar localizado no caminho do servidor indicado***

### Visualizando conversa
Para visualizar a conversa você precisa executar o arquivo do histórico no seu navegador, ou para melhor vizualização e caso esteja dentro de um servidor com APACHE e PHP execute o arquivo ```view.php``` localizado dentro da pasta ```/chat```, exemplo:

    http://192.168.0.1/chat/view.php


***OBS: O arquivo de histórico deve ser indicado na variavel*** ```$conversa = "historic-1.html";``` ***localizada dentro do arquivo*** ```view.php```