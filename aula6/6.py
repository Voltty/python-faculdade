preco = int(input("Qual o preco do produto:"))
formato = int(input("""Qual a forma de pagamento:
[1]À vista em dinheiro ou em cheque(-10%)
[2]À vista no cartão de crédito(-15%)
[3]Duas vezes sem juros(0)
[4]Duas vezes com juros(+10%)
"""))
if formato == 1:
    conta = preco*10/100
    contaF = preco - conta
    print(f"Deu ${contaF} ")
elif formato == 2:
    conta = preco*15/100
    contaF = preco - conta
    print(f"Deu ${contaF} ")
elif formato == 3:
    conta = preco /2
    print(f"Deu duas parcelas de ${conta} ")
elif formato == 4:
    conta = preco*10/100
    contaF = preco + conta
    print(f"Deu ${contaF} ")
