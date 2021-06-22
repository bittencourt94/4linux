from Loja_de_roupas import produtos

mainMenu()


def mainMenu():
    
    While True:
        print("Menu principal")
        print ("1 - Sistema de produtos")
        print("2 - Caixa registradora")
        print("3 - Sair")
        opcao1 =int(input("Digite a opcao: "))
        produtos.produtos
        
        if opcao1 == 1:
            print ("Menu de produtos: ")
            print ("1 - Ver Produtos")
            print ("2 - Adicionar Produtos")
            print ("3 - Remover Produtos")
            print ("4 - Sair")
            opcao2= int(input("Digite a opcao: "))
            
            if opcao2==1:
                produtos.VerProdutos()
            
            elif opcao2==2:
                nome = input("digite um nome: ")
                tamanho = input("digite um tamanho: ")
                preco = float(input("digite um preco: "))
                
                
                produtos.AddProduto(nome,tamanho,preco)
            
            
            elif opcao2==3:
                nome = input("digite o produto que deseja remover: ")
                produtos.RemoveProdutos(nome)
            
            
            elif opcao2==4:
                continue
                
        
        elif opcao1 == 2:
            pass
        
        elif opcao1 == 3:
            break        
    

      
