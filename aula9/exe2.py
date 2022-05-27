import math
raio = float(input("Qual o raio: "))
altura = float(input("Qual a altura: "))
v = math.pi*raio**2*altura
if raio <= 0 or altura <= 0:
    print("Não aceitamos numeros iguais ou menores que zero")
else:
    print(v)