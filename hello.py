#!/usr/bin/env python3

"""Hello Wordl Multi Linguas.

Dependendo da lingua configurada no ambiente correspondente.

Como usar:

Tenha a variável LANG devidamente configurada:

    export LANG=pt_BR   - linux
    set LANG=pt_BR      - Windows


Execução:

    python3 hello.py
    ou 
    ./hello.py

"""
"""

__version__ = "0.0.1"
__author__ = "Alysson Diego"
__license__ = "Unlicense"


import os

current_language = os.getenv("LANG", "pt_BR")[:5]

msg = "Hello World "

if current_language == "pt_BR":
    print("Olá, Mundo!")
elif current_language == "it_IT":
    print("Ciao, Mondo!")
elif current_language == "es_SP":
    print("Hola, Mundo!")
elif current_language == "fr_FR":
    print("Bonjour, Monde!")    
else:
    print("Idioma não suportado.")


dados = ["Alysson", 29, True, None, 95.3]

print(dados)
print(dados.count("Alysson"))
print(dados[:3])
print(dados[1:5])

#para cada info em dados:
for info in dados:
    print("-->", info)
"""





#Enviando uma mensagem/e-mail para uma lista de clientes

email_tmlp = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Este produto é bom em resolver %(texto)s 

Clique agora em %(link)s

Apenas %(quantidade)d disponiveis!

Preço promocional %(preco).2f 
"""

clientes = ["Maria", "João", "Bruno"]

for cliente in clientes:
    print(email_tmlp % {"nome": cliente, 
                        "produto": "caneta", 
                        "texto": "Essa caneta é boa pra anotar xD", 
                        "link": "http://canetasmaneirias.com", 
                        "quantidade": 1, 
                        "preco": 39.90})

print("--------------------")


#OLDSTYLE:

msg = "Olá, %s você é o player n %03d e você tem %.3f pontos"

nome = "Maria"
numero = 3
pontos = 20
msg_formatada = msg % (nome, numero, pontos)

print(msg_formatada) 


#NEWSTYLE:

msg2 = "Olá, {} você é o player n{:03d} e você tem {:.3f} pontos"

nome2 = "Alysson"
numero2 = 4
pontos2 = 20
msg_formatada2 = msg2.format(nome2, numero2, pontos2)

print(msg_formatada2)

#Formatação de Texto
# Centralizar
"{}".format("Alyshow")
"{:^20}".format("Alyshow")
# Esquerda
"{:<20}".format("Alyshow")
#Direita
"{:>20}".format("Alyshow")
 
#Preencher os espaços
"{:*^20}".format("Alyshow")
#'******Alyshow*******'
"{:#^20.3}".format(456.89)
#'######4.57e+02######'
"{:.2f}".format(456.89)
#'456.89'
"{:.4f}".format(456.89)
#'456.8900'
"{:^20.4f}".format(456.90)
#'      456.8900      '
"{:*^20.4f}".format(456.90)
#'******456.9000******'
