import module_crud
from time import sleep

caminho = './projeto_crud_python/arquive/arquive.txt'
conteudo = '\ntexto'

opc1 = 'ler arquivo'
opc2 = 'escrever'
opc3 = 'apagar '
inicia = True

while inicia :

    print('\n'*50)
    print('| ','-'*15,' |')
    print(f'1- {opc1}\n2- {opc2}\n3- {opc3}\n4- sair ->[')
    print('| ','-'*15,' |')
    
    resp = input('?_ ')

    if resp == '1' :

        print('\n'*50)
        print(f'--{opc1.upper()}--')
        print('-'*20,'\n')
        print(module_crud.le(caminho))
        print('\n','-'*20,'\n')
        
        voltar = True
        
        while voltar:
        
            resp2 = input('voltar ?_s or n_ ')
        
            if(resp2 == 's' or resp2 == '1'):
                voltar = False
        
            if(resp2 == 'n' or resp2 == '2'):
                print('saindo...')
                sleep(3.0)
                print('---------')
                voltar = False
                inicia = False
            else:
                print('valor invalido')

    elif resp == '2' :
        
        print('\n'*50)
        print(f'--{opc2.upper()}--')
        print('-'*15)

        resp_2 = True
        
        while resp_2:
        
            resplinnha = str(input('1- na ultima linha\n2- na proxima linha \n?_ '))
            
            if(resplinnha == '1' or resplinnha == '2'):
                print('-'*15,'\n')
                conteudo = str(input('insira o conteudo :\n\n'))
                print('\n')
                print('-'*15)
                print('salvando...')
                print('-'*15)
        
                if(resplinnha == '1'):
                    module_crud.adiciona(conteudo,caminho,True)
        
                if(resplinnha == '2'):
                    module_crud.adiciona(conteudo,caminho,False)
        
                sleep(3.0)
                print('slavo com sucesso!')
        
                quest = True
        
                while quest:
        
                    resp2 = input('voltar ?_s or n_ ')
        
                    if(resp2 == 's' or resp2 == '1'):
                        resp_2 = False
                        quest = False
                    elif(resp2 == 'n' or resp2 == '2'):
                        inicia = False
                        resp_2 = False
                        quest = False
                    else:
                        print('valor invalido')
        
            else:
                print('valor invalido')

    elif resp == '3' :
        
        print('\n'*50)
        print(f'--{opc3.upper()}--')
        module_crud.apaga(caminho)
        print('-'*15)
        print('arquivo apagado !')
        print('-'*15)
        
        voltar = True
        
        while voltar:
        
            resp2 = input('voltar ?_s or n_ ')
        
            if(resp2 == 's' or resp2 == '1'):
                voltar = False
        
            if(resp2 == 'n' or resp2 == '2'):
                print('saindo...')
                sleep(3.0)
                print('---------')
                voltar = False
                inicia = False
            else:
                print('valor invalido')
        
    elif resp == '4' :

        print('saindo...')
        sleep(3.0)
        inicia = False
    else :
        print('seletor não encontrado')