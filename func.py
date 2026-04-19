import time

def init():
    '''
    Cria uma pequena animação de "INICIALIZANDO"
    '''
    for i in 'INICIALIZANDO':
        time.sleep(0.1)
        print(i, end='', flush=True)
    print('\n')
    

def seta():
    '''
    Cria uma animação de uma setinha ">>>"
    '''

    print('')
    for i in '>>> ':
        time.sleep(0.1)
        print(i, end='', flush=True)


def clear():
    '''
    Limpa o terminal

    Limpa a tela inteira
    Move o cursor para a posição (1,1) no topo esquerdo
    '''
    print("\033[2J\033[H", end="", flush=True)



