print(" SEJA BEM VINDO A VINHERIA AGNELLO")
print("***********************************")

ano = 2025

nascimento = input("Digite seu ano de nascimento:")
while not nascimento.isnumeric():
    print("Inválido")
    idade = input("Digite seu ano de nascimento:")
nascimento = int(nascimento)

idade = ano - nascimento
if idade < 18:
    print("Você não tem idade para acessar o nosso site!! ")
else:
    print("    -- Boas compras --    ")
    print("--------------------------")
    print("      VINHOS DA CASA      ")
    print("--------------------------")

    vinho1 = "Pérgola"
    vinho2 = "Tinto"
    vinho3 = "Rosé"
    valor1 = 100
    valor2 = 200
    valor3 = 300


    print("Digite qual vinho você deseja - Seguem as opções a baixo!")

    while True:
        escolha = input(f"-{vinho1} R${valor1}\n"
                        f"-{vinho2} R${valor2}\n"
                        f"-{vinho3} R${valor3}\n"
                        f"-Qual você deseja: ")

        vinhos = [vinho1, vinho2, vinho3]

        if escolha in vinhos:
            print("Adicionado ao carrinho!!")
            break
        else:
            print("Inválido")

    quantidade = input("Quantas garrafas você deseja comprar: ")
    while not quantidade.isnumeric():
        print("Inválido")
        quantidade = input("Quantas garrafas você deseja comprar: ")
    quantidade = int(quantidade)
    print("Adicionado ao carrinho!!")

    if escolha == vinho1:
        preco = valor1 * quantidade
    elif escolha == vinho2:
        preco = valor2 * quantidade
    else:
        preco = valor3 * quantidade

    valor_final = preco
    frete = 25
    localidade = input("Confirme o seu endereço para entrega: ")
    Total = valor_final + frete

    print("-------------------------------")
    continuar = input("Você deseja continuar a compra? Digite Sim ou Não!\n"
                      "- ")

    if continuar == "Não":
        if valor_final > 500:
            print("Frete Grátis!!")
            print(f"O valor total da sua compra foi de R${valor_final}, e será entregue no endereço {localidade}.")
        else:
            print("-------------------------------")
            print(f"O valor total da sua compra foi de R${valor_final} mais o frete de {frete}, totalizando R${Total} e será entregue no endereço {localidade}.")
            print("Muito Obrigado pela sua compra!!")

 #-------------------------------------------------------

    else:

        print("    -- Boas compras --    ")
        print("--------------------------")
        print("      VINHOS DA CASA      ")
        print("--------------------------")

        vinho1 = "Pérgola"
        vinho2 = "Tinto"
        vinho3 = "Rosé"
        valor1 = 100
        valor2 = 200
        valor3 = 300

        print("Digite qual vinho você deseja - Seguem as opções a baixo!")

        while True:
            escolha = input(f"-{vinho1} R${valor1}\n"
                            f"-{vinho2} R${valor2}\n"
                            f"-{vinho3} R${valor3}\n"
                            f"-Qual você deseja: ")

            vinhos = [vinho1, vinho2, vinho3]

            if escolha in vinhos:
                print("Adicionado ao carrinho!!")
                break
            else:
                print("Inválido")

        quantidade = input("Quantas garrafas você deseja comprar: ")
        while not quantidade.isnumeric():
            print("Inválido")
            quantidade = input("Quantas garrafas você deseja comprar: ")
        quantidade = int(quantidade)
        print("Adicionado ao carrinho!!")

        if escolha == vinho1:
            price = valor1 * quantidade
        elif escolha == vinho2:
            price = valor2 * quantidade
        else:
            price = valor3 * quantidade


        valorFinal = valor_final + price
        frete = 25
        total = valorFinal + frete

        if valorFinal > 500:
            print("Frete Grátis!!")
            print(f"O valor total da sua compra foi de R${valorFinal}, e será entregue no endereço {localidade}.")
        else:
            print("-------------------------------")
            print(f"O valor total da sua compra foi de R${valorFinal} mais o frete de {frete}, totalizando R${total} e será entregue no endereço {localidade}.")
            print("Muito Obrigado pela sua compra!!")