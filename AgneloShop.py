print("Seja bem-vindo a Vinheria Agnello!!")


ano = int(input("Digite em que ano você nasceu: "))
idade =  2025 - ano

if idade < 18:
    print("Você deve ter no mímimo 18 anos para acessar o nosso site!! ")

else:
    print("Você tem a idade para acessar o nosso site!! ")

    localidade = input("Digite o seu endereço a baixo: ")

    print("Obrigado, agora faça o pedido do seu vinho a baixo!! ")

    vinho1 = 'Pérgola'
    vinho2 = 'Tinto'
    vinho3 = 'Americano'
    vinho4 = 'Uzumaki'

    preco1 = 120
    preco2 = 150
    preco3 = 200
    preco4 = 250

    vinhos = input(f"Essas são as opções de vinhos:\n"
                   f"- {vinho1} R$ {preco1}\n"
                   f"- {vinho2} R$ {preco2}\n"
                   f"- {vinho3} R$ {preco3}\n"
                   f"- {vinho4} R$ {preco4}\n"
                   f" Qual vinho você deseja? Apenas uma opção!\n").strip().lower()


    quantidade = int(input(f"Quantos vinhos {vinhos} você deseja: "))

    if vinhos == vinho1.lower():
        preco  = preco1
    elif vinhos == vinho2.lower():
        preco = preco2
    elif vinhos == vinho3.lower():
        preco = preco3
    elif vinhos == vinho4.lower():
        preco = preco4
    else:
        print("Vinho não reconhecido! Por favor, tente novamente.")
        exit()

    valor = preco * quantidade

    if valor >= 100:
        print("Compras acima de R$100 não pagam o frete!! Parabéns!!")
        frete = 0
    else:
        frete = 10
        print("Compras a baixo de 100 reais será atribuido um frete de 10 reais!!")

    final = valor + frete

    print(f"Obrigado por comprar com a gente! Você comprou {quantidade} garrafa(s) do vinho {vinhos}, "
          f"totalizando R${final:.2f} {'com frete grátis' if frete == 0 else 'com frete de R$10,00'}.")
    print(f"A sua compra será enviada para: {localidade}")
    print("VOLTE SEMPRE!!!")






