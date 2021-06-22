produtos=[]

def AddProduto(nome,preco):
    
    produto={"Nome": nome,"preco":preco}
    produtos.append(produto)

def VerProdutos:
    for p in produtos:
        print ("=====")
        print(f"Nome: {p['nome']}")
        print(f"Tamanho: {p['tamanho']}")
        print(f"Preco: {p['preco']}")

def RemoveProdutos(nome):
    for p in produtos:
        if p["nome"] == nome:
            produtos.remove(p)
    
    
AddProduto("Camisa Corinthians",  20)
VerProdutos()


    
