print("Vamos calular seu IMC!!!")
P = float(input("Qual o seu peso: "))
A = float(input("Qual a sua altura: "))
IMC = P/A**2
print(f"Seu IMC é {IMC:.2f}")
if IMC >= 18.5 :
    print("Abaixo do peso")
elif IMC >= 18.5 and IMC <=24.9:
    print("Peso normal")
elif IMC >=25 and IMC <= 29.9:
    print("Sobrepeso!!!")
elif IMC >=30 and IMC <=34.9:
    print("Obesidade Grau 1")
elif IMC >=35 and IMC <=39.9:
    print("Obesidade Grau 2")
elif IMC >= 40:
    print("Obesidade Grau 3")
else:
    print("error")