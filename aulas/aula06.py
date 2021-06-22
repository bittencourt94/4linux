def main():
    dic_opcoes= { '1':'consultar','2': 'inserir','3': 'deletar','4':'atualizar','5':'sair'}
    
    while true:
        print("Digiter a opcao desejada: ")
        print("1 - Consultar")
        print("2 - inserir")
        print("3 - deletar")
        print("4 - atualizar")
        print("5 -sair")
        opcao = input(">>> ")
        
        
        if opcao in '12345':
            dic_opcoes[opcao]()
        else:
            print('opcao invalida')

def consultar():
    cpf = input("informe o cpf: ")
    with open('registo.txt','r') as arquivo:
        conteudo = arquivo.readlines()
        for linha in conteudo:
            if cpf in linha.split('\t'):
                registro= linha.split('\t')
                print('CPF',registro[0])
                print('Nome',registro[1])
                print('Idade',registro[2])
                print('Sexo',registro[3])
                print('Nacionalidade',registro[4])
            else:
                print('Registro nao encontrado')
def inserir():
    cpf = input('cpf: ')
    nome = input('nome: ')
    idade = input('idade: ')
    sexo = input('sexo: ')
    nacionalidade = input('nacionalidade: ')
    
    registro = f'{cpf}\t{nome}\t{idade}\t{sexo}\t{nacionalidade}\n'
    with open('registro.txt', 'a+') as arquivo:
        arquivo.write(registro)
        
    
def deletar():
    cpf=input('informe o cpf: ')
    with open('registro.txt','r') as arquivo:
        conteudo = arquivo.readlines()
    for linha in range(0, len(conteudo)):
        if cpf in conteudo[linha].split('\t'):
            registro=conteudo[linha].split('\t')
            print('CPF',registro[0])
            print('Nome',registro[1])
            print('Idade',registro[2])
            print('Sexo',registro[3])
            print('Nacionalidade',registro[4])
            if input('Deseja remover o registro? (S/N)').upper()=='S':
                conteudo.pop(linha)
                with open('registro.txt','w') as arquivo:
                    arquivo.write(''.join(conteudo))
                break
            else:
                print("Cancelado pelo usuario: ")
                break
        else:
             print("Registro nao encontrado")
             break       
                        
              
                


def atualizar():
    cpf = input('informe o cpf: ')
    with open('registro.txt','r') as arquivo:
        conteudo = arquivo.readlines()
    num_registro = 0
    
    while num_registro < len(conteudo):
        if cpf in conteudo[num_registro].split():
            registro = conteudo[num_registro].split('\t')                                
            print('CPF',registro[0])
            print('Nome',registro[1])
            print('Idade',registro[2])
            print('Sexo',registro[3])
            print('Nacionalidade',registro[4])    
            if input('Deseja alterar o registro? (S/N)').upper()=='S':
                registro[0]=input('CPF: ')
                registro[1]=input('Nome: ')
                registro[2]=input('Idade: ')
                registro[3]=input('Sexo: ')
                registro[4]=input('Nacionalidade: ')
                conteudo[num_registro]= '\t'.join(registro)
                
                with open('registro.txt','w') as arquivo:
                    arquivo.write(''.join(conteudo)
                print("Registro atualizado com sucesso")
                break
            else:
                print('Cancelado pelo usuario')
                break                           
        else:
            print('Registro nao encontrado')
            break
 main()
            
