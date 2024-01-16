saraksts = [3, 8, 23, 1, 9]


def skaita():
    summa = 0
    for i in saraksts:
        summa = summa+i
    return summa
    
rez = skaita()
print(rez)
