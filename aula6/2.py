a = int(input("Numero A: "))
b = int(input("Numero B: "))
c = int(input("Numero C: "))
if a+b < c :
    print(a+b)
    print(f"A + B eh menor que C")
elif a+b > c :
    print(a+b)
    print(f"A + B eh maior que C")
else:
    print("erro")
