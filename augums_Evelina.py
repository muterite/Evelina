augumi = {"Valters":172, 
          "Juris":185, 
          "Ausma":164, 
          "Maiga":184, 
          "Ginta":162, 
          "Egita":164, 
          "Māris":165, 
          "Guntis":167, 
          "Viesturs":177, 
          "Raivis":184, 
          "Maija":165, 
          "Melisa":180}

print("Sveiki, šeit ir visi dotie skolēnu augumi:")
for atslega, dati in augumi.items():   # šeit for cikls attiecīgi datiem izprintē katru atslēgas-datu pāri jaunā rindā
    print(atslega, "-", dati, "cm")
print()
print("Ko jūs vēlaties darīt? :")
print("1 - pievienot augumu")
print("2 - izdzēst augumu")
print("3 - iziet no programmas")
atbilde = int(input())

while True:   # kamēr lietotājs ir programmā un ievada datus, programma turpina strādāt, atkārtojot visu 
    if atbilde == 1:  # ja atbilde ir 1, tad lietotājs pievienos datu pāri
        print("Jūs izvēlējāties opciju 1 - pievienot augumu")
        vards = input("Ievadiet skolēna vārdu: ")
        augums = input("Ievadiet skolēna augumu (cm): ")
        print("Jūs pievienojāt", vards, "ar augumu", augums, "cm")
        pievienosana = {vards : augums}  # šeit tiek izveidota jauna vārdnīca, kas vēlāk tiks pievienota galvenajai vārdnīcai "augumi"
        augumi |= pievienosana  # šeit notiek vārdnīcu apvienošana, taču šeit netiek izveidota jauna vārdnīca, bet gan vārdnīca "pievienosana" tiek pievienota "augumi"
        print()
        print("Visi augumi:")
        for atslega, dati in augumi.items():  # šeit for cikls attiecīgi datiem izprintē katru atslēgas-datu pāri jaunā rindā
            print(atslega, "-", dati, "cm")
    elif atbilde == 2:  # ja atbilde ir 2, tad lietotājs dzēsīs datu pāri
        print("Jūs izvēlējāties opciju 2 - izdzēst augumu")
        vards = input("Kuru vārdu jūs vēlaties dzēst? : ")
        print("Tu izdzēsi", vards, "-", augumi[vards], "cm")
        augumi.pop(vards)  # šeit tiek izdzēsts datu pāris, ko izsauc pēc atslēgas, kas šajā gadījumā ir jautāta lietotājam un uzturēta kā mainīgais "vards"
        print()
        print("Visi augumi:")
        for atslega, dati in augumi.items():   # šeit for cikls attiecīgi datiem izprintē katru atslēgas-datu pāri jaunā rindā
            print(atslega, "-", dati, "cm")
    elif atbilde == 3:  # ja lietotājs izvēlas 3, tad programma pateicās par lietošanu un atvadās, kā arī beidz programmu
        print("Jūs izvēlējāties opciju 3 - iziet no programmas")
        print("Paldies, ka izmantojāt šo programmu! Jauku dienu! <3")
        quit()

    print("Ko jūs vēlaties darīt? :")
    print("1 - pievienot augumu")
    print("2 - izdzēst augumu")
    print("3 - iziet no programmas")
    atbilde = int(input())
    


