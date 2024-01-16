print("Jūsu iepirkšanās var sākties!")
atbilde = "nē"
kopeja_summa = 0
kopejais_daudzums = 0
rimi_summa = 0
beta_summa = 0
maxima_summa = 0
top_summa = 0
labais_summa = 0

while atbilde == "nē" :   # izmanto while, jo kamēr nav iegādātas visas preces, jādodas tās nopirkt
    veikals = input("Uz kuru veikalu brauksiet? Izvēles opcijas : Maxima, Rimi, Top, Labais un Beta : ")
    print("Esam atbraukuši! Dodamies iekšā.")
    cena = float(input("Izvēlētās preces cena? "))
    daudzums = int(input("Cik šādas preces? "))

    if cena <= 0 or daudzums <= 0 :   # ja cena vai daudzums ir negatīvi vai 0, tad programma pasaka, ka skaitļi nav pareizi un aizved uz cikla sākumu, lai tos ievadītu atkal
        print("Ievadi pareizus skaitļus.")
        break

    if veikals == "Maxima" :   # ja izvēlētais veikals ir Maxima, tad ir 30% atlaide
        summa = round((cena*daudzums)-(0.3*cena*daudzums),)
        print("Par precēm iztērēji :", summa)
        maxima_summa = maxima_summa+summa

    elif veikals == "Rimi" :   # ja izvēlētais veikals ir Rimi, tad vai nu nav atlaide, vai ir 40% atlaide
        rimi_karte = input("Vai jums ir Rimi karte? (jā/nē) ")
        if rimi_karte == "jā" :   # ja ir Rimi karte, tad atlaide ir 40%
            summa = round((cena*daudzums)-(0.4*cena*daudzums), 2)
        else :   # ja nav Rimi karte, tad nav atlaides
            summa = round(cena*daudzums, 2)
        print("Par precēm iztērēji :", summa)
        rimi_summa = rimi_summa+summa

    elif veikals == "Top" :   # ja izvēlētais veikals ir Top, tad ir vai nu 20% atlaide, vai nu 50% atlaide
        top_karte = input("Vai jums ir Top karte? (jā/nē) ")
        if top_karte == "jā" :   # ja ir Top karte, tad atlaide ir 50%
            summa = round((cena*daudzums)-(0.5*cena*daudzums), 2)
        else :    # ja nav Top karte, tad atlaide ir 20%
            summa = round((cena*daudzums)-(0.2*cena*daudzums), 2)
        print("Par precēm iztērēji :", summa)
        top_summa = top_summa+summa

    elif veikals == "Labais" :  # ja izvēlētais veikals ir Labais, tad ir 30% atlaide, ja pērk 3 preces un vairāk
        if daudzums >= 3 :  # ja daudzums ir lielāks vai vienāds ar 3, tad ir 30% atlaide
            summa = round((cena*daudzums)-(0.3*cena*daudzums), 2)
        else :   # ja daudzums nesasniedz 3, tad nav atlaides
            summa = round(cena*daudzums, 2)
        print("Par precēm iztērēji :", summa)
        labais_summa = labais_summa+summa

    elif veikals == "Beta" :   # ja izvēlētais veikals ir Beta, tad katra otrā prece par brīvu
        x = divmod(daudzums, 2)
        if x == 0 :  # ja dalījuma atlikums ir 0, tad puse no precēm (katra otrā) ir par brīvu
            summa = round((cena*daudzums)-(0.5*cena*daudzums), 2)
        else :   # ja dalījuma atlikums ir cits (1), tad katra otrā prece ir par brīvu, taču tā nebūs puse no visām precēm, tādēļ dalījumu ar 2 noapaļo uz leju un tik preces ir par brīvu (pēc loģikas)
            summa = round((cena*daudzums)-((daudzums//2)*cena), 2)
        print("Par precēm iztērēji :", summa)
        beta_summa = beta_summa+summa

    else :   # ja nav ierakstīts kāds no dotajiem veikaliem, tad programma paziņo, ka tā tādu veikalu nezin
        print("Nezinu tādu veikalu.")

    kopejais_daudzums = kopejais_daudzums+daudzums
    kopeja_summa = maxima_summa + rimi_summa + beta_summa + top_summa + labais_summa
    print("Pašlaik esi iztērējis :", kopeja_summa)
    atbilde = input("Vai esam nopirkuši visas vajadzīgās preces? (jā/nē)")

print()
print()
print("veikalā ""Rimi"" iztērēts :", rimi_summa)
print("veikalā ""Maxima"" iztērēts :", maxima_summa)
print("veikalā ""Top"" iztērēts :", top_summa)
print("veikalā ""Labais"" iztērēts :", labais_summa)
print("veikalā ""Beta"" iztērēts :", beta_summa)
print("-----------------------")
print("Nopirktās preces :", kopejais_daudzums)
print("-----------------------")
print("Kopējā cena :", kopeja_summa)