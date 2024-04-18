import os # biblioteca para poder limpar o terminal

def repeat(value): #function que possibilidade exibir os dados de uma dict em cada linha
    for chave,valor in value.items():
        print (f"{valor}: {chave}")

def choose_user_coin(value_choose): #function que exibe na tela qual foi a moeda escolhida com uma determinada mensagem
    menssage = "Você Escolheu a moeda"
    match value_choose:
        case 1:
            return f"{menssage} Real🪙"
        case 2:
            return f"{menssage} Dolar🪙"
        case 3:
            return f"{menssage} Euro🪙"

def choose_user_convert(response_user_coin): #function que cria uma nova dict com moedas aceitaveis
    dict_secundary = {}
    for chave,valor in coin.items():
        if response_user_coin != valor:
            dict_secundary[chave] = valor
    return dict_secundary

def coin_convert(valeu_one,value_two,value_three): #function que realiza o calculo
    result = value_three
    if valeu_one == 1:
        match value_two:
            case 2:
               result = result * 0.19
            case 3:
                result = result * 0.18
    elif valeu_one == 2:
        match value_two:
            case 1:
                result = result * 5.23
            case 3:
                result = result * 0.93
    elif valeu_one == 3:
        match value_two:
            case 1:
                result = result * 5.59
            case 2:
                result = result * 1.07
    return result

def clear_terminal(): #function que limpa o terminal
    os.system("cls")

def coin_finally(value): #function que exibe qual moeda escolheu com uma determinada mensagem
    match value:
        case 1:
            finally_response = "Reais"
        case 2:
            finally_response = "Dolares"
        case 3:
            finally_response = "Euros"
    return finally_response

coin = { #dict com moedas que o sistema converte
    "REAL" : 1,
    "DOLAR" : 2,
    "EURO" : 3

}

error_numbers_int = "Digite somente números inteiro!⚠️" #variavel que armazena essa string

condicao = True
while condicao: # loop que possibilita recomeçar o programa

    print("Olá, seja bem-vindo(a) a seu conversor de moedas!💰") #começo do programa
    print("Abaixo está a lista das moedas disponíveis para manipular no programa!👇\n")

    repeat(coin) #function que exibe a dict com as moedas que trabalhamos na tela

    while True: #loop da verificação do try...except
        try: #verificação para que aceite somente números inteiros
            response_user_coin = int(input("Escolha qual moeda você irá converter: "))
            if response_user_coin not in coin.values(): #verificação que checa se o dado informado bate com os dados disponíveis
                clear_terminal() #limpeza do terminal
                print("Digite somente números no intervalo de 1 a 3!⚠️\n")
                repeat(coin)
                continue
            break
        except ValueError:
            clear_terminal()
            print(f"{error_numbers_int}\n")
            repeat(coin)
            print()
            continue

    menssage_program = choose_user_coin(response_user_coin) 
    print(f"\n{menssage_program}") #exibição que qual moeda escolheu

    return_program_convert = choose_user_convert(response_user_coin) # atribuição da nova dict a variavel return_program_convert

    while True: #loop do try...except
        try: #validação se está inserindo apenas números
            value_coin = float(input("\nQual valor você irá converter? "))
            break
        except ValueError:
            print("Digite somente números!⚠️ ")

    print(f"\nDe acordo com a lista abaixo:👇")

    print()
    repeat(return_program_convert) #exibição da nova dict com as moedas aceitaveis para converter

    while True: #loop do try...except...
        try: #validação para aceitar apenas números inteiros que estejam disponíveis na nova dict de moedas aceitáveis
            response_user_convert = int(input(f"\nVocê irá converter o valor de {value_coin:.2f} para qual moeda? "))
            if response_user_convert not in return_program_convert.values():
                print("Digite somente as opções disponíveis!⚠️\n")
                print(f"\nDe acordo com a lista abaixo")
                repeat(return_program_convert)
                continue
            break
        except ValueError:
            print(f"{error_numbers_int}")
            print(f"\nDe acordo com a lista abaixo")
            repeat(return_program_convert)
            continue

    menssage_program = choose_user_coin(response_user_convert) 
    print(f"\n{menssage_program}") #exibição que qual moeda escolheu

    can_continue = input("Posso converter?").upper().startswith("S") #permissão para converter

    if can_continue: #condição que converte e exibe na tela
        clear_terminal()        
        value_finally = coin_convert(response_user_coin,response_user_convert,value_coin)  #atribuição do valor Final a uma variavel
        print(f"O valor convertido foi de {value_coin} {coin_finally(response_user_coin)}", end=" ") 
        print(f"para {value_finally:.2f} {coin_finally(response_user_convert)}💵") #exibição dessa variavel
    

    repeat_program = input("Deseja recomeçar?").upper().startswith("S")

    if repeat_program: #condição que possibilita o recomeço do programa
        clear_terminal()
        continue
    else:
        condicao = False
        print("See you later!😊")