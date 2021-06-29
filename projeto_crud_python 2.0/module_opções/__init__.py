import os
from time import sleep
opc1 = 'ler arquivo'
opc2 = 'escrever no arquivo'
opc3 = 'apagar do arquivo'
opc4 = 'sair ->['
opc5 = 'mudar diretorio de texto'

caminho = 'projeto_crud_python 2.0/arquive_texto/arquive.txt'

def opc_1():
    
    print('-'*30)
    arquivo = open(caminho,'r')
    print(arquivo.read())
    arquivo.close()
    print('-'*30)

def opc_2(v_or_f):
    if v_or_f == True:
        arquivo = open(caminho,'a')
        print('-'*30)
        contexto = str(input('digite o texto:\n '))
        print('-'*30)
        arquivo.write(contexto)
        arquivo.close()
        sleep(2.0)
        print('salvo!')
        print('-'*30)
    elif v_or_f == False:
        arquivo = open(caminho,'a')
        print('-'*30)
        contexto = str(input('digite o texto:\n '))
        print('-'*30)
        arquivo.write('\n'+contexto)
        arquivo.close()
        print('salvo!')
        print('-'*30)

def opc_3(v_or_f):
    if v_or_f == True:
        linhas = []
        arquivo = open(caminho,'r')
        for linha in arquivo :
            linhas.append(linha)
        linhas.pop()
        arquivo.close()
        arquivo = open(caminho,'w')
        arquivo.writelines(linhas)
        arquivo.close()
        sleep(2.0)
        print('linha apagada')
        print('-'*30)

    elif v_or_f == False:
        arquivo = open(caminho,'w')
        arquivo.write('')
        arquivo.close()
        sleep(2.0)
        print('arquivo apagado')
        print('-'*30)

def opc_4():
    sleep(2.0)
    print('saindo...')
    print('-'*30)
    return False

def opc_5():
    new_caminho = str(input('insira o novo caminho_ '))
    if os.path.isfile(new_caminho) :
        caminho = new_caminho
        print(f'novo caminho: {caminho}\nadicionado com sucesso')
        print('-'*30)
    else:
        print(f'caminho: {new_caminho} não encontrado')
        print('-'*30)