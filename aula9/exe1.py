num = float(input("Qual o valor: "))
parce = int(input("Quantas parcelas"))

if parce >=6 and parce < 12:
    valor = num +(num*8/100)
    print(f"Você ira pagar R${valor} por parcela")
elif parce >=12 and parce < 24:
    valor = num +(num*23/100)
    print(f"Você ira pagar R${valor} por parcela")
elif parce >=24 and parce < 36:
    valor = num +(num*38/100)
    print(f"Você ira pagar R${valor} por parcela")
else:
    print("Não temos essa opção")



