data= [int(input("Qual o dia:")), int(input("Qual o mes:")), int(input("Qual o ano:"))]
mes =["x","janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
if data[0]>31 or data[0]< 1 :
    print("Esse dia não existe")
    quit()
if data[1]< 1 or data[1]> 12 :
    print("Esse mes não existe")
    quit()
else:
    for i in range(data[1]):
        y = mes[i+1]
print(f"{data[0]} de {y} do ano de {data[2]}")
    
        

