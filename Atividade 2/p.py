def desemprego(self):
        self.__desemprego = self.__ler_nota("Desemprego e desigualdade: ")


def __ler_nota(mensagem):
        print("Informe o grau de relevância de 1 a 5 para cada tópico:")
        while True:
            try:
                nota = int(input(mensagem)) 
                if nota >= 1 and  nota <= 5:
                    return nota
                else:
                    print("Por favor, ensira o valor dentro da faixa permitida:")
            except ValueError:
                print("Por favor, ensira um número válido:")