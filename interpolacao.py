#Enviando uma mensagem/e-mail para uma lista de clientes

#https://pyformat.info/

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
                        
