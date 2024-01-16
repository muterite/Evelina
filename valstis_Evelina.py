valstis = {"Austrija":8978929, 
           "Beļģija":11617623, 
           "Bulgārija":6838937, 
           "Cehija":10516707, 
           "Dānija":5873420, 
           "Francija":67871925, 
           "Grieķija":10459782, 
           "Horvātija":3862305, 
           "Itālija":59030133, 
           "Nīderlande":17590672,}

print("Sveiki, šeit ir visas dotās valstis un to iedzīvotāju skaits:")
print()
for atslega, dati in valstis.items():   # šeit for cikls attiecīgi datiem izprintē katru atslēgas-datu pāri jaunā rindā
    print(atslega, "-", dati, "iedz.")
print()
print("Ko jūs vēlaties darīt? :")
print()
print("1 - sakārtot valstis pēc to nosaukumiem augošā secībā")
print("2 - sakārtot valstis pēc to nosaukumiem dilstošā secībā")
print("3 - sakārtot valstis pēc to iedzīvotāju skaita augošā secībā")
print("4 - sakārtot valstis pēc to iedzīvotāju skaita dilstošā secībā")
print("5 - pievienot jaunu valsti un iedzīvotāju skaitu")
print("6 - apskatīt visas valstis")
print("stop - iziet no programmas")
print()
atbilde = input("Jūsu izvēle: ")
print()

while True:  # kamēr lietotājs ir programmā, programma turpina darbību
    if atbilde == "1":  # ja atbilde ir 1, tad programma sakārto vārdnīcu augošā secībā pēc valstu nosaukumiem
        print("Valstu nosaukumi augošā secībā:")
        print()
        for atslega in sorted(valstis):  # sakārto pēc atslēgas(valsts nosaukuma) augošā secībā, un for cikls izprintē katru datu pāri savā rindā
            print(atslega, "-", valstis[atslega], "iedz.")
    elif atbilde == "2":   # ja atbilde ir 2, tad programma sakārto vārdnīcu dilstošā secībā pēc valstu nosaukumiem
        print("Valstu nosaukumi dilstošā secībā:")
        print()
        for atslega in sorted(valstis, reverse=True):  # sakārto pēc atslēgas(valsts nosaukuma) dilstošā secībā(ar "reverse=True"), un for cikls izprintē katru datu pāri savā rindā
            print(atslega, "-", valstis[atslega], "iedz.")
    elif atbilde == "3":  # ja atbilde it 3, tad programma sakārto vārdnīcu pēc iedzīvotāju skaita augošā secībā
        print("Iedzīvotāju skaits augošā secībā:")
        print()
        kartots = sorted(valstis.items(), key=lambda x:x[1])  # šeit tiek sakārtota vārdnīca "valstis" pēc iedzīvotāju skaita augošā secībā ar "lambda" funkciju
        kartota_vardnica = dict(kartots)
        for atslega, dati in kartota_vardnica.items():   # šeit for cikls attiecīgi datiem izprintē katru atslēgas-datu pāri jaunā rindā 
            print(atslega, "-", dati, "iedz.")
    elif atbilde == "4":   # ja atbilde it 4, tad programma sakārto vārdnīcu pēc iedzīvotāju skaita dilstošā secībā
        print("Iedzīvotāju skaits dilstošā secībā:")
        print()
        kartots = sorted(valstis.items(), key=lambda x:x[1], reverse=True)  # šeit tiek sakārtota vārdnīca "valstis" pēc iedzīvotāju skaita dilstošā secībā(ar "reverse=True") ar "lambda" funkciju
        kartota_vardnica = dict(kartots)  # šeit sakārtoto vārdnīcu, kas pārtapa par ne vārdnīcu kārtošanas laikā, pārdefinē kā vārdnīcu
        for atslega, dati in kartota_vardnica.items():   # šeit for cikls attiecīgi datiem izprintē katru atslēgas-datu pāri jaunā rindā
            print(atslega, "-", dati, "iedz.")
    elif atbilde == "5":   # ja atbilde ir 5, tad programma piedāvā pievienot jaunu valsti un iedzīvotāju skaitu
        print("Pievienot jaunu valsti un iedzīvotāju skaitu:")
        print()
        valsts = input("Ievadi valsts nosaukumu: ")
        if valsts == "stop":   # ja atbilde ir stop, tad programma paziņo par iziešanu, atvadās un iziet no programmas
            print()
            print("Jūs izvēlējāties iziet no programmas")
            print("Paldies ka izvēlējāties mūsu programmu, uz tikšanos! <3")
            exit()
        else:  # ja atbilde nav stop, tad programma turpinās
            iedzivotaji = input("Ievadi valsts iedzīvotāju skaitu: ")
            if iedzivotaji == "stop":  # ja atbilde ir stop, tad programma paziņo par iziešanu, atvadās un iziet no programmas
                print()
                print("Jūs izvēlējāties iziet no programmas")
                print("Paldies ka izvēlējāties mūsu programmu, uz tikšanos! <3")
                exit()
            else:   # ja atbilde nav stop, tad programma turpinās
                print("Jūs pievienojāt", valsts, "ar iedzīvotāju skaitu", iedzivotaji)
                pievienosana = {valsts : int(iedzivotaji)}  # šeit tiek izveidota jauna vārdnīca, kas vēlāk tiks pievienota galvenajai vārdnīcai "valstis"
                valstis |= pievienosana   # šeit notiek vārdnīcu apvienošana, taču šeit netiek izveidota jauna vārdnīca, bet gan vārdnīca "pievienosana" tiek pievienota "valstis"
                for atslega, dati in valstis.items():   # šeit for cikls attiecīgi datiem izprintē katru atslēgas-datu pāri jaunā rindā
                    print(atslega, "-", dati, "iedz.")
    elif atbilde == "6":   # ja atbilde ir 6, tad programma parāda visas valstis
        print("Visas valstis:")
        print()
        for atslega, dati in valstis.items():   # šeit for cikls attiecīgi datiem izprintē katru atslēgas-datu pāri jaunā rindā
            print(atslega, "-", dati, "iedz.")
    elif atbilde == "stop":   # ja atbilde ir stop, tad programma paziņo par iziešanu, atvadās un iziet no programmas
        print("Jūs izvēlējāties iziet no programmas")
        print("Paldies ka izvēlējāties mūsu programmu, uz tikšanos! <3")
        exit()
    print()
    print("Ko jūs vēlaties darīt? :")
    print("1 - sakārtot valstis pēc to nosaukumiem augošā secībā")
    print("2 - sakārtot valstis pēc to nosaukumiem dilstošā secībā")
    print("3 - sakārtot valstis pēc to iedzīvotāju skaita augošā secībā")
    print("4 - sakārtot valstis pēc to iedzīvotāju skaita dilstošā secībā")
    print("5 - pievienot jaunu valsti un iedzīvotāju skaitu")
    print("6 - apskatīt visas valstis")
    print("stop - iziet no programmas")
    print()
    atbilde = input("Jūsu izvēle: ")
    print()

    