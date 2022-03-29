loop = 0
a = 0
b = 0
c = 0
d = 0
ABCDE2 = 0
FGHIJ2 = 0
KLMNO2 = 0
PQRST2 = 0
while loop < 10:
    global ABCDE, ABCDE1, ABCDE3, FGHIJ, FGHIJ1 , FGHIJ3, KLMNO , KLMNO1  , KLMNO3 , PQRST ,PQRST1 , PQRST3
    while a < 5:
        ABCDE = [float(input("Numero grupo 1:"))]
        ABCDE1 = ABCDE[0]
        ABCDE2 += ABCDE1 
        ABCDE3 = ABCDE2/5
        a += 1
        if a == 5:
            print(ABCDE3)
            break
    while b < 5:
        FGHIJ = [float(input("Numero grupo 2:"))]
        FGHIJ1 = FGHIJ[0]
        FGHIJ2 += FGHIJ1
        FGHIJ3 = FGHIJ2/5
        b += 1
        if b == 5:
            print(FGHIJ3)
            break
    while c < 5:
        KLMNO = [float(input("Numero grupo 3:"))]
        KLMNO1 = KLMNO[0]
        KLMNO2 += KLMNO1
        KLMNO3 = KLMNO2/5
        c += 1
        if c == 5:
            print(KLMNO3)
            break
    while d < 5:
        PQRST = [float(input("Numero grupo 4:"))]
        PQRST1 = PQRST[0]
        PQRST2 += PQRST1
        PQRST3 = PQRST2/5
        d += 1 
        loop += 2
        if d == 5:
            print(PQRST3)
            break
        
