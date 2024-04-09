#O código começa com a importação do módulo json. 

import json

#Defini três classes: Profissional, Visitante e Visita. As duas primeiras representam o profissional e visitante cadastrado(a) no sistema, respectivamente. A terceira representa a visita em si, contendo informações sobre o visitante, o profissional visitado e a data/hora de entrada.

class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala

    def get_nome(self):
        return self.__nome

    def get_especialidade(self):
        return self.__especialidade

    def get_sala(self):
        return self.__sala


class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento

    def get_nome(self):
        return self.__nome

    def get_documento(self):
        return self.__documento


class Visita:
    def __init__(self, visitante, profissional, data_entrada):
        self.__visitante = visitante
        self.__profissional = profissional
        self.__data_entrada = data_entrada

    def get_visitante(self):
        return self.__visitante

    def get_profissional(self):
        return self.__profissional

    def get_data_entrada(self):
        return self.__data_entrada

# O método 'cadastrar_profissional()', cadastra um novo profissional no sistema, depois salva as informações no arquivo "profissionais.txt" e adiciona o objeto do profissional à lista 'l_profissionais'.

def cadastrar_profissional():
    nome = input("Nome do profissional: ")
    especialidade = input("Especialidade do profissional: ")
    sala = input("Sala do profissional: ")
    profissional = Profissional(nome, especialidade, sala)
    l_profissionais.append(profissional)
    with open("profissionais.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n{nome}:{especialidade}:{sala}")
        print("Profissional cadastrado com sucesso!")

# O método 'cadastrar_visitante()', cadastra um novo visitante no sistema, depois salva as informações no arquivo "visitantes.txt" e adiciona o objeto do visitante à lista 'l_visitantes'.

def cadastrar_visitante():
    nome = input("Nome do visitante: ")
    documento = input("Documento do visitante: ")
    visitante = Visitante(nome, documento)
    l_visitantes.append(visitante)
    with open("visitantes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n{nome}:{documento}")
        print("Visitante cadastrado com sucesso!")

# O método 'localizar_profissional()', pergunta se a busca é por nome ou por especialidade e, dependendo da resposta, busca e retorna informações do profissional em questão, se encontrado.

def localizar_profissional():
    opcao = input("Deseja localizar o profissional por nome ou especialidade? (n/e): ")
    if opcao.lower() == "n":
        nome = input("Digite o nome do profissional: ")
        for profissional in l_profissionais:
            if profissional.get_nome().lower() == nome.lower():
                print("Nome:", profissional.get_nome())
                print("Especialidade:", profissional.get_especialidade())
                print("Sala:", profissional.get_sala())
                return
        print("Profissional não encontrado.")
    elif opcao.lower() == "e":
        especialidade = input("Digite a especialidade do profissional: ")
        encontrados = []
        for profissional in l_profissionais:
            if profissional.get_especialidade().lower() == especialidade.lower():
                encontrados.append(profissional)
        if encontrados:
            print("Profissionais encontrados com a especialidade", especialidade + ":")
            for profissional in encontrados:
                print("Nome:", profissional.get_nome())
                print("Especialidade:", profissional.get_especialidade())
                print("Sala:", profissional.get_sala())
        else:
            print("Nenhum profissional encontrado com a especialidade", especialidade + ".")
    else:
        print("Opção inválida!")

# O método 'ler_visitantes()', tem como objetivo ler um arquivo chamado "visitantes.txt" e criar uma lista de objetos da classe Visitante, preenchidos a partir das informações contidas no arquivo.

def ler_visitantes():
    visitantes = []
    with open("visitantes.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.strip()
            if linha:
                nome, documento = linha.split(":")
                visitantes.append(Visitante(nome, documento))
    return visitantes

# O método 'ler_profissionais()', lê um arquivo de texto chamado "profissionais.txt" (com codificação UTF-8). O arquivo deve conter informações de profissionais separadas por linha, onde cada linha apresenta o formato "nome:especialidade:sala" (sendo "nome", "especialidade" e "sala" informações distintas).

def ler_profissionais():
    profissionais = []
    with open("profissionais.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.strip()
            if linha:
                nome, especialidade, sala = linha.split(":")
                profissionais.append(Profissional(nome, especialidade, sala))
    return profissionais

# O método 'registrar_visita()' pede ao usuário as informações necessárias para registrar uma nova visita e faz a validação dessas informações. Depois, salva a visita no dicionário 'dict_visitas'.

def registrar_visita():
    l_visitantes = ler_visitantes()
    l_profissionais = ler_profissionais()

    nome_visitante = input("Digite o nome do visitante: ")
    nome_profissional = input("Digite o nome do profissional: ")
    data_entrada = input("Digite a data de entrada: ")

    visitante = None
    for v in l_visitantes:
        if v.get_nome().lower() == nome_visitante.lower():
            visitante = v
            break
    if visitante is None:
        print("Visitante não encontrado.")
        return

    profissional = None
    for p in l_profissionais:
        if p.get_nome().lower() == nome_profissional.lower():
            profissional = p
            break
    if profissional is None:
        print("Profissional não encontrado.")
        return

    documento = visitante.get_documento()
    if documento in dict_visitas.keys() and dict_visitas[documento]["nome_profissional"].lower() == nome_profissional.lower():
        print("Essa visita já foi registrada anteriormente.")
        return

    dict_visitas[documento] = {
        "nome_profissional": profissional.get_nome(),
        "hora_entrada": data_entrada,
        "sala": profissional.get_sala()
    }
    print("Visita registrada com sucesso!")

# O método 'relatorio_conferencia()', pede o nome de um profissional e busca no dicionário 'dict_visitas' o registro de todas as visitas realizadas por visitantes ao profissional informado.

def relatorio_conferencia():
    nome_profissional = input("Digite o nome do profissional: ")
    for visitante_documento, visita_data in dict_visitas.items():
        if visita_data["nome_profissional"].lower() == nome_profissional.lower():
            visitante = None
            for v in l_visitantes:
                if v.get_documento() == visitante_documento:
                    visitante = v
                    break
            if visitante is not None:
                print("Visitante:", visitante.get_nome())
                print("Data da visita:", visita_data["hora_entrada"])
                print("------------------")
    print("Fim do relatório.")

# O método 'gerar_arquivo_registros()', cria um arquivo "registros_dia.json" contendo as informações de todas as visitas registradas em um dia específico.

def gerar_arquivo_registros():
    with open("registros_dia.json", "w") as arquivo:
        json.dump(dict_visitas, arquivo)
    print("Arquivo de registros do dia gerado com sucesso!")

# O método 'ler_arquivos()', lê dois arquivos de texto, "profissionais.txt" e "visitantes.txt", usando codificação "utf-8" e cria objetos "Profissional" e "Visitante" com base nas informações de cada linha do arquivo. As instâncias de objetos criadas são adicionadas às listas "l_profissionais" e "l_visitantes", respectivamente.

def ler_arquivos():
    # Lendo o arquivo "profissionais.txt"
    with open("profissionais.txt", "r", encoding="utf-8") as arquivo:
        # Pegando todas as linhas do arquivo
        linhas = arquivo.readlines()
        # Iterando sobre cada linha
        for linha in linhas:
        # Removendo espaços em branco no início e no final da linha
            linha = linha.strip()
        # Ignorando linhas em branco
            if linha:
        # Separando os campos através do caractere ":"
                profissional_data = linha.split(":")
        # Criando um objeto Profissional com os campos extraídos
                profissional = Profissional(profissional_data[0], profissional_data[1], profissional_data[2])
        # Adicionando o objeto Profissional à lista l_profissionais
                l_profissionais.append(profissional)

    # Lendo o arquivo "visitantes.txt"
    with open("visitantes.txt", "r", encoding="utf-8") as arquivo:
        # Pegando todas as linhas do arquivo
        linhas = arquivo.readlines()
        # Iterando sobre cada linha
        for linha in linhas:
        # Removendo espaços em branco no início e no final da linha
            linha = linha.strip()
        # Ignorando linhas em branco
            if linha:
        # Separando os campos através do caractere ":"
                visitante_data = linha.split(":")
        # Criando um objeto Visitante com os campos extraídos
                visitante = Visitante(visitante_data[0], visitante_data[1])
        # Adicionando o objeto Visitante à lista l_visitantes
                l_visitantes.append(visitante)

l_profissionais = []
l_visitantes = []
dict_visitas = {}
ler_arquivos()

# O programa termina com um loop em que o usuário escolhe uma das sete opções do menu apresentado na tela. Cada escolha chama a função correspondente. O loop continua até o usuário digitar '7', quando o programa se encerra.

while True:
    print("======================")
    print("MENU")
    print("======================")
    print("1- Cadastrar Profissional")
    print("2- Cadastrar Visitante")
    print("3- Localizar Profissional")
    print("4- Registrar Visita")
    print("5- Relatório de Conferência")
    print("6- Gerar arquivo de Registros do dia")
    print("7- Sair")
    escolha = input("Escolha: ")

    if escolha == "1":
        cadastrar_profissional()
    elif escolha == "2":
        cadastrar_visitante()
    elif escolha == "3":
        localizar_profissional()
    elif escolha == "4":
        registrar_visita()
    elif escolha == "5":
        relatorio_conferencia()
    elif escolha == "6":
        gerar_arquivo_registros()
    elif escolha == "7":
        break
    else:
        print("Opção inválida!")

print("Fim do programa.")
