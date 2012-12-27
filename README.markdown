#dShortener

Um encurtador de URLs feito em Django

##Quero ver funcionando, como faço?

Obtenha-o
```shell
$ git clone https://github.com/douglasmiranda/dshortener.git
```

e então... (eu suponho que você use virtualenv/virtualenvwrapper e pip)
```shell
$ cd dshortener

$ mkvirtualenv dshortener --no-site-packages
$ workon dshortener

$ pip install -r requirements.txt

$ cd dshortener

$ ./manage.py syncdb
$ ./manage.py runserver
# Tah Dah, é pra funcionar daí =]
```

se não usa virtualenv/virtualenvwrapper e pip, (shame on you), então...
```shell
$ cd dshortener

# Instale como bem entender o que está em requirements.txt

$ cd dshortener
$ ./manage.py syncdb
$ ./manage.py runserver
# Tah Dah, é pra funcionar daí tbm... mas ainda acho que você deve aprender sobre virtualenv/virtualenvwrapper e pip :P
```

PS: É bem simples, daí você pode usar sua criatividade e implementar um contador e/ou outras estatísticas. Quando criar o diferencial do seu encurtador de URLs, basta lancá-lo e ficar milionário. =D