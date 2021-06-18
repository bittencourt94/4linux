nome = input ("Digite o seu nome: ")
idade = input ("Digite sua idade: ")
email = input ("Digite seu e-mail: ")
telefone = input ("Digite seu telefone: ")


while 1==1:
    print (f'Bem vindo {nome}!')
    print ("1 - Exiba todas as informações")
    print ("2 - Exiba nome e idade")
    print ("3 - Exiba seu email e telefone")
    print ("0 - Sair")
    escolha = int(input(">>> "))
    if escolha == 1:
        print(f"{nome} , {idade}, {email} , {telefone}")
        continue
    elif escolha == 2:
        print(f"{nome} , {idade}")
        continue
    elif escolha == 3:
        print(f"{email} , {telefone}")
        continue
    elif escolha == 0:
        break
    else:      
        print ("Opção inexistente!")
        
        
   # Exercicios Apostila

# 1

# data = int(input('Digite o ano de nascimento: '))


# if data <= 1964:
#     print('Baby Boomer')
# elif data >= 1965 and data <= 1979:
#     print('Geração X')
# elif data >= 1980 and data <= 1994:
#     print('Geração Y')
# elif data >= 1995:
#     print('Geração Z')
# else:
#     print('Informe uma data valida')

# 2 - Quitanda
cesta = []
total = 0

while True:
    print('Quitanda:')
    print('1 - ver cesta')
    print('2 - Adicionar fruta')
    print('3 - checkout')
    print('4 - Sair')
    opcao = int(input('Digite a Opção: '))
    if opcao == 1:
        for item in cesta:
            print(f"Produto: {item['nome']}, Valor: {item['valor']}")
    elif opcao == 2:
        print('Menu de frutas:')
        print('1 - Banana')
        print('2 - Caju')
        print('3 - Manga')
        print('4 - Abacaxi')
        banana = {'nome':'banana', 'valor': 1.50}
        caju = {'nome':'caju', 'valor': 4.50}
        manga = {'nome':'manga', 'valor': 2.50}
        abacaxi = {'nome':'abacaxi', 'valor': 5.00}
        fruta = int(input('Digite a Opção: '))
        if fruta == 1:
            cesta.append(banana)
        elif fruta == 2:
            cesta.append(caju)
        elif fruta == 3:
            cesta.append(manga)
        elif fruta == 4:
            cesta.append(abacaxi)
        else:
            print('Opção invalida')
    elif opcao == 3:
        print('Checkout')
        for item in cesta:
            total += item['valor']
        print(f'Total da Compra: {total}')
        break

        # print(f'Valor total: {}')

    elif opcao == 4:
        break
     
             
                
            
    

