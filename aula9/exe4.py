data= [int(input("Qual o dia:")), int(input("Qual o mes:")), int(input("Qual o ano:"))]
mes =["X","janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
def checkdata():
    if data[0]>31 or data[0]< 1 :
        print("Esse dia não existe")
        quit()
    if data[1]< 1 or data[1]> 12 :
        print("Esse mes não existe")
        quit()
if True:
    checkdata()
    for i in range(data[1]):
        y = mes[i+1]
        z = i + 1 
    if z == 4 or z == 6 or z == 9 or z == 11:
        if data[0] <= 31 and data[0] > 1:
            checkdata()
            print(f"{data[0]} de {y} do ano de {data[2]}")
        else:
            print("Esse mes não tem esse dia")
    if z == 1 or z == 3 or z == 5 or z == 7 or z == 8 or z == 10 or z == 12:
        if data[0] <= 30 and data[0] > 1:
            checkdata()
            print(f"{data[0]} de {y} do ano de {data[2]}")
        else:
            print("Esse mes não tem esse dia")
    if z == 2:
        if data[0] <= 29 and data[0] > 1:
            checkdata()
            print(f"{data[0]} de {y} do ano de {data[2]}")
        else:
            print("Esse mes não tem esse dia")
