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

"""print(dados)
print(dados.count("Alysson"))
print(dados[:3])
print(dados[1:5])
"""
#para cada info em dados:
for info in dados:
    print("-->", info)

