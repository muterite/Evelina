pasazieri = int(input("Cik pasažieri? ")) 
if pasazieri > 4 :  # ja pasažieri ir vairāk par 4, tad taksī nav vieta un 
    print("Pārāk liels cilvēku skaits priekš taksometra pakalpojumiem.")
else :   # ja taksī ir mazāk vai 4 cilvēki, tad turpinās programma
    plkst = int(input("Cik ir pulkstens?(0-24h) "))
    if plkst >=0 and plkst < 6 :  # ja pulkstens ir 22:00-5:59, tad tarifs ir lielāks
        tarifs = float(0.67)
    elif plkst >= 22 and plkst <=24 :
        tarifs = float(0.67)
    elif plkst >= 6 and plkst <22 :  # ja pulkstens ir 6:00-21:59, tad tarifs ir mazāks
        tarifs = float(0.57)
    else :
        exit("Sāc no jauna un ievadi pareizus datus.")
    vieta = input("Vai taksis ir stāvvietā pie stacijas?(jā/nē) ")
    if vieta == "jā" :  # ja taksis atrodas stāvvietā, tad ir tikai nolīgšanas cena 
        noligsana = 1.25
    elif vieta =="nē" :   # ja taksis nav stāvvietā, tad nolīgšanas cenai klāt nāk arī izsaukšanas cena
        noligsana = 1.25+2.20
    else :
        exit("Sāc no jauna un ievadi pareizus datus.")
    gaidisana = input("Vai taksometram nāksies jūs gaidīt?(jā/nē) ")
    if gaidisana == "jā" :   # ja taksometram būs jāgaida persona, tad tiek jautāts uz cik minūtēm
        gaidisanas_minutes = int(input("Cik minūtes? "))
    elif gaidisana == "nē" :  # ja taksometram nav jāgaida presona, tad nav jēga jautāt cik ilgi būtu jāgaida, jo nebūs jāgaida
        gaidisanas_minutes = 0
    else :
        exit("Sāc no jauna un ievadi pareizus datus.")
    gaidisanas_cena = round(gaidisanas_minutes*0.13, 2)
    km = int(input("Cik kilometrus būs jābrauc? "))
    kopeja_cena = round((tarifs*km)+noligsana+gaidisanas_cena, 2)
    print()
    print("Cena par kilometru : ", tarifs,"€", "| Kilometri :", km, "| Kopā :", round(tarifs*km, 2),"€")
    print()
    print("Cena par gaidīšanu (1 min) : 0.13€", "| Gaidīts :", gaidisanas_minutes, "min", "| Kopā : ", gaidisanas_cena, "€")
    print()
    print("Nolīgšanas cena : ", noligsana, "€")
    print()  
    print("Kopējā cena par braucienu :", kopeja_cena, "€")  
    # visi print, kas ir pēdējās rindās ir veidoti lai glīti izkārtotos un būtu labi pārredzams "čeks"