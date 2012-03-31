#Processo seletivo Globo.com - Desafio

Desafio proposto como parte do processo de seleção Globo.com

##Descrição do problema

Desenvolva uma aplicação web para encurtar urls (como o http://goo.gl/). Alguns casos de aceite:

* Cadastro e autenticação simples de usuário;

* Usuário ou anônimo cadastra uma url e tem como retorno ela encurtada:
      Entrada: http://g1.globo.com saida: localhost:5000/xpto

* Usuário ao se logar verá todas as urls que ele cadastrou.

* Ao acessar a url encurtada (localhost:8000/xpto), o usuário deve ser redirecionado para a url relacionada (http://g1.globo.com)