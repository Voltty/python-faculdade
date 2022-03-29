loop = 0
im = 0
pm = 0 
am = 0
while loop <= 9:
    global i , imf , a , amf , p ,pmf
    pessoa = [float(input("altura: ")) , float(input("Idade: ")) , float(input("Peso: "))]
    i = pessoa[1]
    im += i
    imf = im/10
    a = pessoa[0]
    am += a
    amf = am/10
    p = pessoa[2]
    pm += p
    pmf = pm/10
    loop += 1
else:
    print(f"A idade media é: {imf}, a altura media é: {amf} e o peso medio é:{pmf}")