#O código começa importando a biblioteca json e a classe datetime da biblioteca datetime, para lidar com datas e horas.

import json
from datetime import datetime

#A classe Veiculo, que possui três atributos: placa, hora_entrada e hora_saida;
# sendo que a hora de entrada é preenchida automaticamente com o valor da data e hora atual, enquanto que a hora de saída é deixada em branco.

class Veiculo:
    def __init__(self, placa):
        self.placa = placa
        self.hora_entrada = datetime.now()
        self.hora_saida = None

#A classe Estacionamento, que tem um atributo chamado vagas. Este atributo é um 
# dicionário que contém números de vagas de 1 a 40 como chaves e uma lista vazia como valor correspondente.

class Estacionamento:
    def __init__(self):
        self.vagas = {i: [] for i in range(1, 41)}

#Dentro desta classe, temos três funções: estacionar, saida e resumo_ocupacao.
#A função estacionar recebe um veículo como parâmetro e percorre o dicionário de vagas. 
# Quando encontra uma vaga livre (ou seja, que está com uma lista vazia),
# adiciona o veículo na lista desta vaga e retorna o número da vaga. Caso contrário, o método retorna None.

    def estacionar(self, veiculo):
        for vaga, carros in self.vagas.items():
            if not carros:
                carros.append(veiculo)
                return vaga
        return None

#A função saida recebe a placa do veículo como parâmetro e percorre o dicionário de vagas, 
# procurando um veículo cuja placa seja igual à placa recebida. Se encontra um veículo assim, 
# atualiza a hora de saída deste veículo com o valor atual da data e hora,
# remove o veículo da lista da vaga e retorna o número da vaga. Caso contrário, o método retorna None.

    def saida(self, placa):
        for vaga, carros in self.vagas.items():
            for carro in carros:
                if carro.placa == placa:
                    carro.hora_saida = datetime.now()
                    carros.remove(carro)
                    return vaga
        return None

#A função resumo_ocupacao percorre o dicionário de vagas e exibe na tela o número da vaga,
# a placa do veículo estacionado nela, a hora de entrada e, se houver, a hora de saída.

    def resumo_ocupacao(self):
        for vaga, carros in self.vagas.items():
            print(f"Vaga {vaga}:")
            if not carros:
                print("Vaga livre")
            else:
                for carro in carros:
                    print(f"Placa: {carro.placa} - Entrada: {carro.hora_entrada.strftime('%d/%m/%Y %H:%M:%S')}", end="")
                    if carro.hora_saida is not None:
                        print(f" - Saída: {carro.hora_saida.strftime('%d/%m/%Y %H:%M:%S')}")
                    else:
                        print(" - Ainda estacionado")

#A função verificar_arquivo verifica se o tipo de arquivo é "TXT" ou "JSON" e dependendo do tipo de arquivo, 
# tenta abrir o arquivo correspondente em modo de leitura, e retorna esse conteúdo como uma string. 

def verificar_arquivo(tipo_arquivo):
    if tipo_arquivo.upper() == "TXT":
        try:
            with open("estacionamento.txt", "r") as arquivo_txt:
                return arquivo_txt.read()
        except FileNotFoundError:
            print("Arquivo TXT não encontrado.")
    elif tipo_arquivo.upper() == "JSON":
        try:
            with open("estacionamento.json", "r") as arquivo_json:
                return arquivo_json.read()
        except FileNotFoundError:
            print("Arquivo JSON não encontrado.")
    else:
        print("Tipo de arquivo inválido.")

estacionamento = Estacionamento()

#O loop while True executa um menu de opções para o usuário, a fim de que ele possa estacionar um veículo, 
# retirar um veículo, verificar a ocupação do estacionamento e sair do programa.

while True:
    print("=== Estacionamento do Tio Ivo ===")
    print("1- Estacionar")
    print("2- Saída")
    print("3- Resumo de ocupação")
    print("9- Fim")
    escolha = input("Escolha: ")

    if escolha == "1":
        placa = input("Digite a placa do veículo: ")
        veiculo = Veiculo(placa)
        vaga = estacionamento.estacionar(veiculo)
        if vaga:
            print(f"O veículo foi estacionado na vaga {vaga}")
        else:
            print("Não há vagas disponíveis")

    elif escolha == "2":
        placa = input("Digite a placa do veículo que deseja retirar: ")
        vaga = estacionamento.saida(placa)
        if vaga:
            print(f"O veículo foi retirado da vaga {vaga}")
        else:
            print("Veículo não encontrado")

    elif escolha == "3":
        estacionamento.resumo_ocupacao()

#Se o usuário escolhe a opção 9, o programa pergunta se ele deseja salvar os dados em um arquivo TXT ou JSON. 
# Se ele escolhe TXT, é criado um arquivo de texto chamado "estacionamento.txt" 
# e nele são gravadas as informações sobre as vagas e os veículos estacionados.
# Se a escolha for JSON, é criado um arquivo JSON chamado "estacionamento.json" e nele são gravadas as informações do dicionário de vagas.

#Se o usuário digitar um tipo de arquivo inválido, o código emite uma mensagem de erro. 
# Se o usuário escolher não salvar os dados em um arquivo, o código retorna "Opção inválida". 
# Em ambos os casos, o código termina a execução com o comando break.

    elif escolha == "9":

        resposta = input("Deseja salvar os dados em um arquivo TXT ou JSON? (S/N) ")
        if resposta.upper() == "S":
            tipo_arquivo = input("Digite o tipo de arquivo que deseja salvar (TXT ou JSON): ")
            if tipo_arquivo.upper() == "TXT":
                with open("estacionamento.txt", "w") as arquivo_txt:
                    for vaga, carros in estacionamento.vagas.items():
                        arquivo_txt.write(f"Vaga {vaga}:\n")
                        if not carros:
                            arquivo_txt.write("Vaga livre\n")
                        else:
                            for carro in carros:
                                arquivo_txt.write(f"Placa: {carro.placa} - Entrada: {carro.hora_entrada.strftime('%d/%m/%Y %H:%M:%S')}\n")
                                if carro.hora_saida is not None:
                                    arquivo_txt.write(f" - Saída: {carro.hora_saida.strftime('%d/%m/%Y %H:%M:%S')}\n")
                                else:
                                    arquivo_txt.write(" - Ainda estacionado\n")
                print("Dados salvos no arquivo TXT.")
            elif tipo_arquivo.upper() == "JSON":
                with open("estacionamento.json", "w") as arquivo_json:
                    json.dump(estacionamento.vagas, arquivo_json, default=str)
                print("Dados salvos no arquivo JSON.")
            else:
                print("Tipo de arquivo inválido")
        break

    else:
        print("Opção inválida")
