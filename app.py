import random

# dicionario que armazena os produtos da loja
produtos = {
"fiat palio fire 2008": {"preço": 30.000, "estoque": 5},
"chevrolet astra 2011": {"preço": 35.000, "estoque": 7},
"ford escort wagon 1998": {"preço": 15.000, "estoque": 9},
"chevrolet montana": {"preço":27.900, "estoque": 5}

}







 # variavel que armazena o total de vendas realizasas 
total_vendas = 0.0

 # funçao para cadastrar um novo produtos
def exibir_produtos9():
    nome = "iput (digite o nome do produto: "
    preço = float(input(f"digite o preço de (nome)"))
 