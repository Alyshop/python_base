#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.
"""
__version__ = "0.1.0"
__author__ = "Alyssão"

#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(base[2])


numeros = list(range(1, 11))  # Cria uma lista de números de 1 a 10 (range não inclui o 11)

for numero in numeros:  # Para cada número na lista 'numeros'
    print("Tabuada do:", numero)  # Imprime qual tabuada está sendo exibida
    for outro_numero in numeros:  # Para cada número novamente na lista 'numeros'
        print(numero * outro_numero)  # Imprime o resultado da multiplicação entre 'numero' e 'outro_numero'