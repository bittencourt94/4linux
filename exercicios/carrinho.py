carrinho = []

def verCarrinho():
    for c in carrinho:
        print ("=====")
        print(f"Nome: {c['nome']}")
        print(f"Tamanho: {c['tamanho']}")
        print(f"Preco: {c['preco']}")

def addProdutoCarrinho(produto):
    carrinho.append(produto)
    print(carrinho)

def removeProdutoCarrinho(produto):
    for c in carrinho:
        if c["nome"] == produto:
            carrinho.remove(c)
            
def checkout():
    total=0
    for c in carrinho:
        total+= c["preco"]
    print(f" Total: {total}")
                    
                        
