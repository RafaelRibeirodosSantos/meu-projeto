from module_opções import *

def formatado(opções,v_f,title):
    if v_f :
        print('-'*30)
        print(f'{title.center(30)}')
        print('-'*30)
        n1 = 1
        for opção in opções:        
            print('\033[1;33m',f'{n1}- \033[1;34m{opção}','\033[0;0m')
            n1 += 1
        print('-'*30)
    else:
        print('-'*30)
        n1 = 1
        for opção in opções:        
            print('\033[1;33m',f'{n1}- \033[1;34m{opção}','\033[0;0m')
            n1 += 1
        print('-'*30)

def interface():
    #loop responsavel pelo funcionamento da interface
    inicia = True
    while inicia:
        formatado([opc1,opc2,opc3,opc4,opc5],True,'MENU PRINCIPAL')
        opção = str(input('?_ '))
        if opção == '1':
            opc_1()
            quest = True
            while quest:
                resp2 = input('voltar ?_s or n_ ')
                if(resp2 == 's' or resp2 == '1'):
                    quest = False
                elif(resp2 == 'n' or resp2 == '2'):
                    quest = False
                    inicia = False
                else:
                    print('valor invalido')
        if opção == '2':
            quest = True
            while quest:
                formatado(['escrever na ultima linha','escrever na proxima linha'],False,'')
                resp = str(input('?_ '))
                if resp == '1':
                    opc_2(True)
                    quest = False
                elif resp == '2':
                    opc_2(False)
                    quest = False
                else:
                    print('opção invalida')
            quest2 = True
            while quest2:
                resp2 = input('voltar ?_s or n_ ')
                if(resp2 == 's' or resp2 == '1'):
                    quest2 = False
                elif(resp2 == 'n' or resp2 == '2'):
                    quest2 = False
                    inicia = False
                else:
                    print('valor invalido')
        if opção == '3':
            quest = True
            while quest:
                formatado(['apagar ultima linha','apagar tudo'],False,'')
                resp = str(input('?_ '))
                if resp == '1':
                    opc_3(True)
                    quest = False
                elif resp == '2':
                    opc_3(False)
                    quest = False
                else:
                    print('opção invalida')
            quest = True
            while quest:
                resp2 = input('voltar ?_s or n_ ')
                if(resp2 == 's' or resp2 == '1'):
                    quest = False
                elif(resp2 == 'n' or resp2 == '2'):
                    quest = False
                    inicia = False
                else:
                    print('valor invalido')
        if opção == '4':
            if opc_4() == False:
                break
        if opção == '5':
            opc_5()
            quest = True
            while quest:
                resp2 = input('voltar ?_s or n_ ')
                if(resp2 == 's' or resp2 == '1'):
                    quest = False
                elif(resp2 == 'n' or resp2 == '2'):
                    quest = False
                    inicia = False
                else:
                    print('valor invalido')