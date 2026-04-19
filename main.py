from class_aln import Aluno, Alunos
from func import init, seta, clear
from funcs_doc import func_doc as doc
import os

# Descobre o caminho da pasta onde main.py está
caminho = os.path.dirname(os.path.abspath(__file__))

# Junta o caminho da pasta com o nome de 'alunos.csv'
caminho_alunos_csv = os.path.join(caminho, 'alunos.csv')

# Junta o caminho da pasta com o nome do 'funcs_list.txt'
caminho_funcs_list_txt = os.path.join(caminho, 'funcs_list.txt')


alunos = Alunos(caminho_alunos_csv)

alunos_list = alunos.load_arqv()

aln = {}

#Iniciando o prorama
init()

while True:

    seta()

    op = input('')
    infs = op.split()

    print('')

    #EXIBIR INFORMAÇÕES

    #EXIBIR INFORMAÇÕES GERAIS
    if op == 'aln info':
        alunos.aln_info()

    elif op == 'aln info /doc' or op == 'aln_info /doc':
        doc(Alunos.aln_info)

    #EXIBIR TABELA DE ALUNOS
    elif op == 'aln tab':
        print(alunos.alns_tab().to_string(index=False))

    elif op == 'aln tab /doc' or op == 'alns_tab /doc':
        doc(Alunos.alns_tab)
    
    #EXIBIR LISTA DE ALUNOS(EM ORDEM DE ID)
    elif op == 'aln lst':
        alunos.lista_alns()
    
    #DOCUMENTAÇÃO: 
    elif op == 'aln lst --doc' or op == 'lista_alns /doc':
        doc(Alunos.lista_alns)

    #EXIBE LISTA DE ALUNOS EM ORDEM ALFABÉTICA
    elif op == 'aln lst ord alpha':
        alunos.lista_alns_ord_alpha()
    
    elif op == 'aln lst ord alpha /doc' or op == 'lista_aln_ord_alpha /doc':
        doc(Alunos.lista_aln_ord_alpha)
    

    #AÇÕES

    #CRIA ALUNO: crate aln "nome" "turma" "numero" "email" "teste_psic" "teste_prof" "teste_matur"
    elif len(infs) >= 9 and op[0:11] == 'create aln ':
        try:
            nome_completo = " ".join(infs[2:-6]) 

            novo_id = max([int(i.i_d) for i in alunos_list], default=-1) + 1

            aln[nome_completo] = Aluno(str(novo_id), nome_completo, infs[-6], infs[-5], infs[-4], infs[-3], infs[-2], infs[-1])

            if not aln[nome_completo] in alunos_list:
                alunos.save_aln(aln[nome_completo])
            else:
                print('ERRO::COMAND: create aln --> Aluno já existente')

        except Exception as erro:
            print(erro)
    
    #DOCUMENTAÇÃO
    elif op == 'create aln /doc' or op == 'seve_aln /doc':
        doc(Alunos.save_aln)
    

    #EDITAR ALUNO: edit aln id 1 | chave: valor
    elif op[:12] == 'edit aln id ' and infs[3].isdigit() and infs[4] == '|' and len(infs) >= 7 and infs[3] in [i.i_d for i in alunos_list]:

        match infs[5]:

            #EDITAR A: edit aln id 1 | nome: nome do aluno
            case 'nome:':
                alunos.edit_aln('NOME', infs[3], ' '.join([inf for inf in infs[6:]]))

            
            #EDITAR ALUNOS: edit aln id 1 | turma: nome da turma (ex.: sampi)
            case 'turma:':
                alunos.edit_aln('TURMA', infs[3], ' '.join([inf for inf in infs[6:]]))
            
            #EDITAR ALUNOS: edit aln id 1 | numero: numero (ex.: +5566997865454)
            case 'numero:':
                alunos.edit_aln('NUMERO', infs[3], ''.join([inf for inf in infs[6:]]))
            
            #EDITAR ALUNOS: edit aln id 1 | email: email (ex.: exemplo.email@gmai.com)
            case 'email:':
                alunos.edit_aln('EMAIL', infs[3], infs[6])
            
            #EDITAR ALUNOS: edit aln id 1 | teste_psic: teste_psic (ex.: 1-c:2-a)
            case 'teste_psic:':
                alunos.edit_aln('TESTE PSIC', infs[3], infs[6])
            
            #EDITAR ALUNOS: edit aln id 1 | teste_prof: teste_prof (ex.: 2)
            case 'teste_prof:':
                alunos.edit_aln('TESTE PROF', infs[3], infs[6])
            
            #EDITAR ALUNOS: edit aln id 1 | teste_matur: teste_matur (ex.: 1-a:2-c)
            case 'teste_matur:':
                alunos.edit_aln('TESTE MATUR', infs[3], infs[6])
            
            case _:
                print('erro')
    
    #DOCUMENTAÇÃO
    elif op == 'edit aln /doc' or op == 'edit_aln /doc':
        doc(Alunos.edit_aln)

    
    #REMOVER ALUNO:
    elif op[:14] == 'remove aln id ' and len(infs) == 4 and infs[3].isdigit():
        alunos.remove_aln(infs[3])
    
    #DOCUMENTAÇÃO
    elif op == 'remove aln /doc' or op == 'remove_aln /doc':
        doc(Alunos.remove_aln)

    
    #BUSCAS

    #BUSCAR ALUNOS POR ID
    elif op[:16] == 'buscar aln id = ' and len(infs) == 5 and infs[4].isdigit():
        print(alunos.buscar_por_id(str(infs[4])).to_string(index=False))
    
    #DOCUMENTAÇÃO
    elif op == 'buscar aln id /doc' or op == 'buscar_por_id /doc':
        doc(Alunos.buscar_por_id)
    
    #BUSCAR ALUNOS POR NOME
    elif op[:18] == 'buscar aln nome = ' and len(infs) == 5 and infs[4].isalpha():
        print(alunos.buscar_por_nome(str(infs[4].upper())).to_string(index=False))
    
    #DOCUMENTAÇÃO
    elif op == 'buscar aln nome /doc' or op == 'buscar_por_nome /doc':
        doc(Alunos.buscar_por_nome)
    
    #EXIBE LISTA DE COMANDOS
    elif op == 'comands lst' or  op == 'help':
        with open(caminho_funcs_list_txt, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            print(conteudo)
    
    #LIMPAR TERMINAL
    elif op == 'clear':
        clear()
    
    #DOCUMENTAÇÃO
    elif op == 'clear /doc':
        doc(clear)

    #SAIR DO PROGRAMA
    elif op == 'exit':
        exit()
    

    #CASO O USUÁRIO DIGITE O COMANDO ERRADO
    else:
        print('ERRO : COMANDO NÃO ENCONTRADO')
