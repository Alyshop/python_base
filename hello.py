#!/usr/bin/env python3
"""
__version__ = "0.0.1"
__author__ = "Alysson Diego"
__license__ = "Unlicense"

"""
import os

current_language = os.getenv("LANG", "pt_BR")[:5]

msg = "pokedex em us"
print(msg)

if current_language == "pt_BR":
    print("pokedex em br")
elif current_language == "it_IT":
    print("Ciao, Mondo")
 