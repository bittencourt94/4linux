# Criar uma aplicação de Calculo de média


# Entradas:
    # nome do aluno
    # n1 - nota número 01
    # n2 - nota número 02
    # n3 - nota número 03
    # n4 - nota número 04
# Saída:
    # Retornar a média do aluno no formato:
    
    # Nome do aluno
    # Nota final]
    
    
nome = input("Digite o nome do aluno: ")
n1 = float(input ("Digite a nota 1 do aluno: "))
n2 = float(input ("Digite a nota 2 do aluno: "))
n3 = float(input ("Digite a nota 3 do aluno: "))
n4 = float(input ("Digite a nota 4 do aluno: "))
media= (n1+n2+n3+n4)/4
print ("O aluno",nome,"tem media ",media)


