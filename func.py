import time

def init():
    '''
    Cria uma pequena animação de "inicializando...."
    '''
    for i in 'INICIALIZANDO':
        time.sleep(0.1)
        print(i, end='', flush=True)
    print('\n')
    

def seta():
    '''
    Cria uma animação de uma setinha
    >>>
    '''
    print('')
    for i in '>>> ':
        time.sleep(0.1)
        print(i, end='', flush=True)

def clear():
    # \033[2J limpa a tela inteira
    # \033[H move o cursor para a posição (1,1) no topo esquerdo
    print("\033[2J\033[H", end="", flush=True)

'''
def type_num(texto):
    try:
        num = float(texto)
        if num.is_integer():
            return "int"
        return "float"

    except ValueError:
        return "Não é um número"
        print(i, end='')
'''
