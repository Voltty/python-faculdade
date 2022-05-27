salario = float(input("Seu salario: "))
if salario <= 1710.78:
    print(f"Seu salario liquido eh {salario:.2f}")
elif salario >= 1710.79 and salario <= 2563.91:
    sal_liq = (salario*7.5/100) 
    sal_liqF = salario - sal_liq  
    print(f"Seu salario liquido eh {sal_liqF:.2f}")
elif salario >= 2563.92 and salario <= 3418.59:
    sal_liq = (salario*15/100) 
    sal_liqF = salario - sal_liq  
    print(f"Seu salario liquido eh {sal_liqF:.2f}")
elif salario >= 3418.60 and salario <= 4271.59:
    sal_liq = (salario*22.5/100) 
    sal_liqF = salario - sal_liq  
    print(f"Seu salario liquido eh {sal_liqF:.2f}")
elif salario >= 4271.60:
    sal_liq = (salario*27.5/100) 
    sal_liqF = salario - sal_liq
    print(f"Seu salario liquido eh {sal_liqF:.2f}")
else:
    print("erro")