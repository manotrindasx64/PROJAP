import os
# Bloqueia o motor gráfico ANTES de qualquer outro import pesado
os.environ["QT_QPA_PLATFORM"] = "offscreen" 
os.environ["QT_LOGGING_RULES"] = "*.debug=false;qt.qpa.*=false" # Silencia logs extras do Qt

import pandas as pd
import csv
import time



class Aluno:
    def __init__(self, i_d: str, nome: str, turma: str, numero: str, email: str, teste_psic: str, teste_prof: int, teste_matur: str):
        self.__i_d = i_d
        self.__nome = nome
        self.__turma = turma
        self.__numero = numero
        self.__email = email
        self.__teste_psic = teste_psic
        self.__teste_prof = teste_prof
        self.__teste_matur = teste_matur
    

    @property
    def i_d(self):
        
        '''Retorna id '''
        
        return self.__i_d
    

    @property
    def nome(self):
        
        '''Retorna nome '''
        
        return self.__nome
    

    @nome.setter
    def nome(self, nv_arg: str):
        
        '''Troca o atributo 'nome' do objeto '''
        
        if not isinstance(nv_arg, str):
            raise TypeError("O nome deve ser uma string!")
        else:
            self.__nome = nv_arg
    

    @property
    def turma(self):
        
        '''Retorna turma '''
        
        return self.__turma
    

    @turma.setter
    def turma(self, nv_arg: str):
        
        '''Troca o atributo 'nome' do objeto '''
        
        if not isinstance(nv_arg, str):
            raise TypeError("A turma deve ser uma string!")
        else:
            self.__turma = nv_arg
    

    @property
    def numero(self):
        
        '''Retorna numero '''
        
        return self.__numero
    

    @numero.setter
    def numero(self, nv_arg: str):

        '''Troca o atributo 'nome' do objeto '''

        if not isinstance(nv_arg, str):
            raise TypeError("O numero deve ser uma string!")
        else:
            self.__numero = nv_arg
    
    @property
    def email(self):
        
        '''Retorna email '''
        
        return self.__email
    
    @email.setter
    def email(self, nv_arg: str):

        '''Troca o atributo 'email' do objeto '''

        if not isinstance(nv_arg, str):
            raise TypeError("O email deve ser uma string!")
        else:
            self.__email = nv_arg

    @property
    def teste_psic(self):
        
        '''Retorna o atributo teste_psic '''
        
        return self.__teste_psic
    

    @teste_psic.setter
    def teste_psic(self, nv_arg: str):

        '''Troca o atributo 'teste_psic' do objeto '''

        if not isinstance(nv_arg, str):
            raise TypeError("O teste_psic deve ser uma string!")
        else:
            self.__teste_psic = nv_arg
    
    @property
    def teste_prof(self):

        '''Retorna nome '''
        
        return self.__teste_prof

    @teste_prof.setter
    def teste_prof(self, nv_arg: str):

        '''Troca o atributo 'teste_prof' do objeto '''

        if not isinstance(nv_arg, str):
            raise TypeError("O teste_prof deve ser uma string!")
        else:
            self.__teste_prof = nv_arg
    

    @property
    def teste_matur(self):
        
        '''Retorna o atributo teste_matur '''
        
        return self.__teste_matur
    

    @teste_matur.setter
    def teste_matur(self, nv_arg: str):

        '''Troca o atributo 'teste_matur' do objeto '''

        if not isinstance(nv_arg, str):
            raise TypeError("O teste_matur deve ser uma string!")
        else:
            self.__teste_matur = nv_arg
    
    
    def aln_exib(self):

        '''Exibe todos os atributos do objeto '''

        print(f'ID: {self.__i_d}', end=' ')
        print(f'NOME: {self.__nome}', end=' ')
        print(f'| TURMA: {self.__turma}', end=' ')
        print(f'| NUMERO: {self.__numero}', end=' ') 
        print(f'| EMAIL: {self.__email}', end=' ') 
        print(f'| TESTA PSIC: {self.__teste_psic}', end=' ')
        print(f'| TESTE PROF: {self.__teste_prof}', end=' ')
        print(f'| TESTE MATUR: {self.__teste_matur}')


class Alunos:
    def __init__(self, arquivo):
        self.__arquivo = arquivo
        
    def load_arqv(self):

        '''Carrega o arquivo .csv '''
        
        alns = []

        with open(self.__arquivo, mode='r', encoding='utf-8') as f:
            leitor = csv.reader(f)
            for linha in leitor:
                aln = Aluno(str(linha[0]), linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7])
                alns.append(aln)
        return alns
    

    def save_aln(self, aln):

        ''' Salva o aluno adcionando uma nova linha(entidade) no arquivo '''

        with open(self.__arquivo, mode='a', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow([
                str(aln.i_d).upper(), 
                aln.nome.upper(), 
                aln.turma.upper(), 
                aln.numero.upper(), 
                aln.email.upper(), 
                aln.teste_psic.upper(), 
                aln.teste_prof.upper(), 
                aln.teste_matur.upper()
            ])
    
    #MÉTODO EDITAR ALUNO
    def edit_aln(self, col_nome: str, id_procurado: str, valor_troca: str):

        '''Edita uma linha espacífica do arquivo '''

        dados_finais = []
        
        alterou = False # Flag de segurança
        
        with open(self.__arquivo, 'r', newline='', encoding='utf-8') as f:
            leitor = csv.reader(f)
            
            cols = ['NOME', 'TURMA', 'NUMERO', 'EMAIL', 'TESTE PSIC', 'TESTE PROF', 'TESTE MATUR']
            
            posicao = int(cols.index(col_nome.upper())) + 1
            
            for linha in leitor:
                if linha:
                    if linha[0] == id_procurado:
                        linha[posicao] = valor_troca.upper()
                        alterou = True # Avisa que achou e alterou
                dados_finais.append(linha)
        
        # SÓ GRAVA SE REALMENTE FEZ ALTERAÇÃO
        if alterou:
            with open(self.__arquivo, 'w', newline='', encoding='utf-8') as f:
                escritor = csv.writer(f)
                escritor.writerows(dados_finais)
        
        else:
            print("ID não encontrado. Nada foi alterado.")

    
    #MÉTODO REMOVER ALUNO
    def remove_aln(self, id_para_remover: str):

        '''Remove uma linha do arquivo '''

        # Lista que armazenará todos os alunos, exceto o que será removido
        dados_finais = []
        encontrado = False
        
        # O ID deve ser tratado como string e em maiúsculo para bater com o save_aln
        id_busca = str(id_para_remover).upper()

        # 1. Leitura e filtragem
        with open(self.__arquivo, 'r', newline='', encoding='utf-8') as f:
            leitor = csv.reader(f)
            for linha in leitor:
                if linha: # Garante que a linha não está vazia

                    # Comparamos o ID buscado com a primeira coluna do arquivo
                    if linha[0] == id_busca:
                        encontrado = True
                        continue # Pula esta linha (não adiciona à lista final)
                    
                    dados_finais.append(linha)
        

        #REESCRIA DO ARQUIVO
        if encontrado:
            with open(self.__arquivo, 'w', newline='', encoding='utf-8') as f:
                escritor = csv.writer(f)
                escritor.writerows(dados_finais)

            print(f"Sucesso: Aluno com ID {id_busca} removido.") #Avisa que o ID foi encontrado e que o aluno foi removido
        
        else:
            print(f"Aviso: O ID {id_busca} não foi encontrado.") #Avisa que o ID não foi encontrado, resultando na não remoção
    

    def alns_tab(self):

        '''Gera a tabela de alunos convertendo a lista de objetos em um Data Frame'''

        # Transforma a lista de objetos obtida em load_arqv() em um Data Frame
        df = pd.DataFrame([
            {
                'ID': str(obj.i_d),
                'NOME': obj.nome,
                'TURMA': obj.turma,
                'NUMERO': obj.numero,
                'EMAIL': obj.email,
                'TESTE PSIC': obj.teste_psic,
                'TESTE PROF': obj.teste_prof,
                'TESTE MATUR': obj.teste_matur
            } for obj in self.load_arqv()
        ])

        return df
    

    #MÉTODO BUSCAR POR ID
    def buscar_por_id(self, id_buscado: str):

        '''Realisa consulta através do id'''

        df = self.alns_tab()

        # Retorna apenas a linha onde o ID coincide
        resultado = df[df['ID'] == str(id_buscado)]
        
        return resultado

    
    # MÉTODO BUSCAR POR NOME
    def buscar_por_nome(self, nome_buscado: str):

        '''Realisa consulta através do nome'''

        # Carrega o Data Frame de alunos
        df = self.alns_tab()

        # Retorna apenas as linhas onde o nome coincide
        resultado = df[df['NOME'] == str(nome_buscado)]
        
        return resultado
    
    
    # MÉTODO LISTA DE ALUNOS
    def lista_alns(self):

        '''Gera  uma lista de alunos(nomes) ordenada pelo id'''

        # Carrega o Data Frame de alunos
        df = self.alns_tab()
        
        #Verifica se o Data Frame está vazio para e
        if df.empty:
            print("Nenhum aluno cadastrado.")
            return
        
        for i in 'LISTA DE ALUNOS':
            print(i, end='', flush=True)
            time.sleep(0.05)
        print('\n')

        # Pega a coluna NOME, converte para lista
        nomes = df['NOME'].astype(str).tolist()
        
        for nome in nomes:
            print(nome)
            time.sleep(0.05)

    
    def lista_alns_ord_alpha(self):

        '''Gera uma lista de alunos(nomes) em ordem alfabética'''

        # Carrega o Data Frame de alunos
        df = self.alns_tab()
        
        # Verifica se o DF está vazio e evitando problemas com o sorted()
        if df.empty:
            print("Nenhum aluno cadastrado.")
            return
        
        for i in 'LISTA DE ALUNOS':
            print(i, end='', flush=True) # Cria uma simple animação de "LISTA DE ALUNOS" no output
            time.sleep(0.05)
        print('\n')

        # Pega a coluna NOME, converte para lista e ordena
        nomes_ordenados = sorted(df['NOME'].astype(str).tolist())
        

        for nome in nomes_ordenados:
            print(nome)
            time.sleep(0.05) # Cria uma simple animação da lsita de alunos no output
    
    # MÉTODO ALN INFO: GERA INFORMAÇÕES GERAIS A RESPEITOS DOS ALUNOS
    def aln_info(self):

        '''Exibe infomações gerais dos alunos'''

        df = self.alns_tab()
        
        print('INFORMAÇÕES:')
        print(f'\nQUANTIDADE DE ALUNOS: {len(df)}')

        # Exibe média geral de "TESTE PROF"
        print(f'\nMÉDIA GERAL TESTE PROF: {(sum([int(i) for i in df['TESTE PROF']])/len(df['TESTE PROF'])):.2f}')

        # Mostra f
        print(f'\n{(df['TESTE PSIC'].value_counts(normalize=True) * 100).map("{:.2f}%".format)}') 
        print(f'\n{(df['TESTE PROF'].value_counts(normalize=True) * 100).map("{:.2f}%".format)}')
        print(f'\n{(df['TESTE MATUR'].value_counts(normalize=True) * 100).map("{:.2f}%".format)}\n')

