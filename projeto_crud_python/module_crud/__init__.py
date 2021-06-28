def adiciona(conteudo_,caminho_,ultima=True):
    
    if(ultima == True):
        arquivo_de_texto = open(caminho_,'a')
        arquivo_de_texto.write(conteudo_)
        arquivo_de_texto.close()
    
    if(ultima == False):
        arquivo_de_texto = open(caminho_,'a')
        conteudo_final = '\n'+conteudo_
        arquivo_de_texto.write(conteudo_final)
        arquivo_de_texto.close()

def reescreve(conteudo_,caminho_):
    arquivo_de_texto = open(caminho_,'w')
    arquivo_de_texto.write(conteudo_)
    arquivo_de_texto.close()

def apaga(caminho_):
    arquivo_de_texto = open(caminho_,'w')
    arquivo_de_texto.write('')
    arquivo_de_texto.close()

def le(caminho_):
    arquivo_de_texto = open(caminho_,'r')
    
    array_linhas = arquivo_de_texto.readlines()
    texto_completo = ''
    for linha in array_linhas :
        texto_completo += linha

    arquivo_de_texto.close()
    return texto_completo