def zvaigznites(skaits):   # definēju funkciju "zvaigznites", kas izprintē "skaits" daudzumu ar zvaigznītēm
    for i in range(skaits):  # for cikls iziet 55 reizes, un katru reizi tas izprintē 1 zvaigznīti, kā arī end funkcija un komats pēc tās nodrošina, ka starp zvaigznītēm nebūs atstarpes un zvaigznītes būs vienā rindā
        print("*", end="",)

def galvene():   # definēju funkciju "galvene", kas izprintē virsrakstu un zvaigznīšu rindu ar 55 zvaigznītēm
    print("Faktoriāla aprēķināšana")
    print(zvaigznites(55))
 
def faktorials(skaitlis):   # definēju funkciju "faktorials", kas aprēķina skaitļa faktoriālu un izprintē to
    rezultats = 1
    for i in range(1,skaitlis+1):  # for cikls aprēķina faktoriālo skaitli, katru ciklu reizinot esošo rezultātu ar nākamo skaitli, līdz pēdējam skaitlim
        rezultats = rezultats*i
    print("Faktoriāls:", rezultats)

def tuksums():
    print()
    print()

galvene()
while True:  # while cikls kurā True ir vienmēr True, lai programma ietu uz apli
    ievade = int(input("Ievadiet veselu, pozitīvu skaitli (mazāku par 13): "))
    if ievade>0 and ievade<13:  # ja ievadītais skaitlis der vajadzīgajos parametros, tad programma aprēķina faktoriālo skaitli
        faktorials(ievade)
    else:  # ja ievadītais skaitlis neder parametriem, tad programma to paziņo
        print("Ievadītais skaitlis nav derīgs!")
    
    turpinat = input("Vai vēlaties turpināt darbu? (jā/nē): ")
    if turpinat == "jā":  # ja lietotājs vēlas turpināt, tad cikls sākas no jauna
        tuksums()
        continue
    else :  # ja lietotājs vēlas beigt, tad programma atsveicinās un beidz darboties
        tuksums()
        print("Paldies, ka izmantojāt šo programmu!")
        quit()
