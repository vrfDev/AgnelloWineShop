print("Seja bem-vindo a Vinheria Agnello!!")


while True:
    try:
        ano = int(input("Digite em que ano você nasceu: "))
        idade =  2025 - ano

        if idade < 18:
            print("Você deve ter no mímimo 18 anos para acessar o nosso site!! ")
        else:
            print("Você tem a idade para acessar o nosso site!!")
            break

    except ValueError:
        print("Por favor, digite um número válido!")

while True:
    localidade = input("Digite o seu endereço a baixo: ")
    if localidade.isnumeric():
        print("Endereço inválido! Por favor, insira o endereço corretamente!!")
    else:
        break


vinho1 = 'Pérgola'
vinho2 = 'Tinto'
vinho3 = 'Americano'
vinho4 = 'Uzumaki'

preco1 = 120
preco2 = 150
preco3 = 200
preco4 = 250

vinhos_validos = [vinho1.lower(), vinho2.lower(), vinho3.lower(), vinho4.lower()]

while True:
    vinhos = input(f"Essas são as opções de vinhos:\n"
                   f"- {vinho1} R$ {preco1}\n"
                   f"- {vinho2} R$ {preco2}\n"
                   f"- {vinho3} R$ {preco3}\n"
                   f"- {vinho4} R$ {preco4}\n"
                   f" Qual vinho você deseja? Apenas uma opção!\n").strip().lower()

    if vinhos in vinhos_validos:
        break
    else:
        print("Vinho não reconhecido! Por favor, escolha um vinho válido.")

while True:
    try:
        quantidade = int(input(f"Quantos vinhos {vinhos} você deseja: "))
        break
    except ValueError:
        print("Por favor, digite um número válido.")

if vinhos == vinho1.lower():
    preco  = preco1
elif vinhos == vinho2.lower():
    preco = preco2
elif vinhos == vinho3.lower():
    preco = preco3
else:
    preco = preco4

valor = preco * quantidade

if valor >= 200:
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






