import math as m

def insert_dado(value_insert): # fuction que possibilita o armazenamento de dados

    coeficiente_tratado = value_insert() # atribuição dos coeficientes tratados em uma variavel
    return coeficiente_tratado # retornando essa variavel ao chamar a function

def tratamento_dado(): # function para capturar os dados e tratar

        while True: # function que captura o coeficiente A e trata para não ser zero

            try:
                a = float(input("Coeficiente A:"))
                if a == 0:
                    print("O coeficiente A, não pode receber o valor igual a zero!")
                    continue
                break
            except:
                print("Digite somente números!")
                continue

        while True: # function para tratar o coeficiente B

            try:
                b = float(input("Coeficiente B:"))
                break
            except:
                print("Digite somente números!")
                continue

        while True: # function para tratar o coeficiente C

            try:
                c = float(input("Coeficiente C:"))
                break
            except:
                print("Digite somente números!")
                continue

        dado_tratado = [a,b,c]
        return dado_tratado

def calculo_delta(value): # function que calcula o delta
    
    delta = ((value[1] * value[1]) - (4 * value[0] * value[2]))
    return delta

def calculo_bhaskara(value_delta): # function que realiza o calculo final do teorema de bhaskara

    if value_delta > 0:
        calculo_final = []
        x = captura_coeficientes_tratado # atribuição dos valores dos coeficientes a uma variavel

        x1 = (-x[1] + m.sqrt(value_delta)) / (2 * x[0])
        calculo_final.append(x1)

        x2 = (-x[1] - m.sqrt(value_delta)) / (2 * x[0])
        calculo_final.append(x2)
    
    elif value_delta < 0:
        calculo_final = ("Esses valores determinou em Raízes Complexas!")

    else:
        calculo_final = ("Esta equação nao possui raízes reais")

    return calculo_final
        
def exibicao_final(calculo_bhaskara): # exibição da equação por linha
    cont = 0 # criação dessa variavel para imprimir qual "X" da equação pertence a qual valor
    if isinstance(calculo_bhaskara, str):
        print(calculo_bhaskara)
    else:
        print("\nO resultado final é")
        for i in calculo_bhaskara:
            cont += 1
            print(f"X{cont}:{i:.2f}", sep="\n")

while True: # operador de repetição caso o usuário deseje recomeçar o programa

    print("Seja Bem vindo(a) ao seu Teorema de Bhaskara Digital!\n") # começo do programa
    print("Digite por gentileza os coeficientes!")

    captura_coeficientes_tratado = insert_dado(tratamento_dado) # atribuição dos coeficientes tratados a uma variavel

    value_delta = calculo_delta(captura_coeficientes_tratado) # atribuição do valor do delta a uma variavel

    calculo_final = calculo_bhaskara(value_delta) # atribuição do valor a uma variavel

    exibicao_final(calculo_final) # exibição do valor final

    resposta = input("\nDeseja recomeçar:") # possibilidade de recomeçar o programa
    resposta_trat = resposta.lower().startswith("s")

    if resposta_trat:
        print()
        continue
    else:
        print("Até mais!😊\n")
        break

