class Relevancia:
    def __init__(self):
        self.__desemprego = None
        self.__etica = None
        self.__seguranca = None
        self.__regulamentacao = None
        self.__potencial = None

pesquisa = {}

estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO',
'RR', 'SC', 'SP', 'SE', 'TO']

def realizar_avaliacao():
    while True:
        estado = input("Informe o estado em que você reside de acordo com sua sigla: ").upper()
        if estado not in estados:
            print("Estado inválido, tente novamente!")
        else:
            break
        
    relevancia = Relevancia()
    
    print("Informe o grau de relevância de 1 a 5 para cada tópico:")
    while True:
        try:
            relevancia.__desemprego = int(input("Desemprego e desigualdade: ")) 
            if relevancia.__desemprego >= 1 and  relevancia.__desemprego <= 5:
                break
            else:
                print("Por favor, ensira o valor dentro da faixa permitida:")
        except ValueError:
            print("Por favor, ensira um número válido:")

    while True:
        try:
            relevancia.__etica = int(input("Questões éticas e morais: ")) 
            if relevancia.__etica >= 1 and  relevancia.__etica <= 5:
                break
            else:
                print("Por favor, ensira o valor dentro da faixa permitida: ")
        except ValueError:
            print("Por favor, ensira um número válido:")  

    while True:
        try:
            relevancia.__seguranca = int(input("Segurança cibernética e privacidade: "))
            if relevancia.__seguranca >= 1 and  relevancia.__seguranca <= 5:
                break
            else:
                print("Por favor, ensira o valor dentro da faixa permitida: ")
        except ValueError:
            print("Por favor, ensira um número válido:")   
    
    while True:
        try:
            relevancia.__regulamentacao = int(input("Controle e regulamentação: ")) 
            if relevancia.__regulamentacao >= 1 and  relevancia.__regulamentacao <= 5:
                break
            else:
                print("Por favor, ensira o valor dentro da faixa permitida: ")
        except ValueError:
            print("Por favor, ensira um número válido:")
            
    while True:
        try:
            relevancia.__potencial = int(input("Potencial desenvolvimento de IA superinteligente: ")) 
            if relevancia.__potencial >= 1 and  relevancia.__potencial <= 5:
                break
            else:
                print("Por favor, ensira o valor dentro da faixa permitida: ")
        except ValueError:
            print("Por favor, ensira um número válido:")    
    
    if estado in pesquisa:
        pesquisa[estado].append(relevancia)
    else:
        pesquisa[estado] = [relevancia]
    
    print("Avaliação registrada com sucesso!")

def relatorio():
    while True:
        estado = input("Informe o estado para ver o relatório de importância: ").upper()
        if estado not in estados:
            print("Estado inválido, tente novamente!")
        else:
            break
    
    if estado in pesquisa:
        relevancias = pesquisa[estado]
        total_avaliacoes = len(relevancias)
        
        soma_desemprego = sum(avaliacao.__desemprego for avaliacao in relevancias)
        media_desemprego = soma_desemprego / total_avaliacoes
        
        soma_etica = sum(avaliacao.__etica for avaliacao in relevancias)
        media_etica = soma_etica / total_avaliacoes
        
        soma_seguranca = sum(avaliacao.__seguranca for avaliacao in relevancias)
        media_seguranca = soma_seguranca / total_avaliacoes
        
        soma_regulamentacao = sum(avaliacao.__regulamentacao for avaliacao in relevancias)
        media_regulamentacao = soma_regulamentacao / total_avaliacoes
        
        soma_potencial = sum(avaliacao.__potencial for avaliacao in relevancias)
        media_potencial = soma_potencial / total_avaliacoes
        
        print(f"Relatório de importância para o estado {estado}: ")
        print(f"Desemprego e desigualdade: {media_desemprego:.2f}")
        print(f"Questões éticas e morais: {media_etica:.2f}")
        print(f"Segurança cibernética e privacidade: {media_seguranca:.2f}")
        print(f"Controle e regulamentação: {media_regulamentacao:.2f}")
        print(f"Potencial desenvolvimento de IA superinteligente: {media_potencial:.2f}")
    else:
        print("Nenhum dado encontrado para o estado informado.")

while True:
    print("\nMenu")
    print("0- Finalizar o Programa")
    print("1- Realizar avaliação")
    print("2- Relatório")
    
    escolha = input("Escolha: ")
    
    if escolha == "0":
        break
    elif escolha == "1":
        realizar_avaliacao()
    elif escolha == "2":
        relatorio()
    else:
        print("Opção inválida. Tente novamente.")

print("Programa finalizado.")
