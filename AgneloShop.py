print("===Seja bem-vindo(a)==")

nome = input("Agnello-> Como devemos te chamar?\n->")

ano = input(f"{nome}, por favor digite seu ano de nascimento: \n->")

while not ano.isnumeric():
    print("!!RESPOSTA INVÁLIDA!!!")
    ano = input(f"{nome}, por favor digite seu ano de nascimento: \n->")

idade = 2025 - int(ano)

vinho_1 = "Adamantino"
vinho_2 = "Tarantino"
vinho_3 = "Pescalino"

preco_vinho_1 = 50
preco_vinho_2 = 60
preco_vinho_3 = 230

qtn_vinho_1 = 0
qtn_vinho_2 = 0
qtn_vinho_3 = 0

frete = 5.00
promo = 500

sair = 'sair'
comprar = 'continuar'

if idade >= 18:
    carrinho = 0
    while True:
        print(f"Carrinho: R${carrinho:.2f}")

        print(f"""Agnello-> Este é o nosso menu:
            =========MENU========
            R${preco_vinho_1:.2f} - {vinho_1} |
            R${preco_vinho_2:.2f} - {vinho_2}  |
            R${preco_vinho_3:.2f} - {vinho_3} |
            ======================
        """)
        pedido = input("Agnello-> Digite sua escolha de vinho\n->").lower()

        while not (pedido == vinho_1.lower() or pedido == vinho_2.lower() or pedido == vinho_3.lower()):
            print("Só serão aceitos os itens presentes em nosso menu!!")
            pedido = input("Agnello-> Digite sua escolha de vinho\n->").lower()

        qnt = input("Agnello-> Quantas garrafas você deseja?\n->")

        while not qnt.isnumeric():
            print("!!RESPOSTA INVÁLIDA!!!")
            qnt = input("Agnello-> Quantas garrafas você deseja?\n->")

        qnt = int(qnt)
        compra = qnt

        if pedido == vinho_1.lower():
            compra *= preco_vinho_1
            qtn_vinho_1 += qnt
        elif pedido == vinho_2.lower():
            compra *= preco_vinho_2
            qtn_vinho_2 += qnt
        else:
            compra *= preco_vinho_3
            qtn_vinho_3 += qnt

        carrinho += compra

        finalizar = input("Agnello-> Deseja continuar a compra? (Digite 'sair' ou 'continuar')\n->").lower()

        while not (finalizar == comprar or finalizar == sair):
            print("!!RESPOSTA INVÁLIDA!!!")
            finalizar = input("Agnello-> Deseja continuar a compra? (Digite 'sair' ou 'continuar')\n->")

        if finalizar == comprar:
            continue
        else:
           break

    endereco = input("Agnello-> Digite seu endereço\n->")
    if carrinho > promo:
        print("VOCÊ GANHOU FRETE GRÁTIS!!!")
        frete = 0
    else:
        carrinho += frete

    print(f"""
        =========Carrinho========
        {vinho_1} - {qtn_vinho_1} |
        {vinho_2} - {qtn_vinho_2} |
        {vinho_3} - {qtn_vinho_3} |
        frete - R$ {frete}
        total - R$ {carrinho:.2f}
        Endereço - {endereco}
        ======================
    Agnello-> {nome}, Muito obrigado por comprar com a gente!! Até a próxima!!""")
else:
    print(f"{nome}, a venda de bebidas alcoolicas para menores de idade não é permitida!!")
