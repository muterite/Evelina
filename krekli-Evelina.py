def pasuti_tkreklus(skaits, apdruka, piegade):  # definē funkciju pasuti_tkreklus, kas iekļauj visu prasīto no specifikācijas, kā arī veic galvenos aprēķinus
    summa=0
    kreklu_summa=0
    piegades_maksa=0
    if apdruka == "TEKSTS" :  # if un elif reģistrē atbildes, ko iedod lietotājs, un no tām aprēķina kreklu summu, balstoties uz apdrukas veida un tā cenas
        kreklu_summa= round(skaits*5, 2)
    elif apdruka =="ZIME" :
        kreklu_summa= round(skaits*7, 2)
    elif apdruka =="FOTO" :
        kreklu_summa=round(skaits*10, 2)

    if kreklu_summa > 100 :  # ja kreklu summa ir lielāka par 100 euro, tad 5% atlaide tiek piemērota pasūtījuma summai
        kreklu_summa=kreklu_summa-(kreklu_summa*0.05)

    if kreklu_summa > 50 :  # ja kreklu summa ir lielāka par 50 euro, piegāde ir False (par piegādi nav jāmaksā)
        piegade=False
        piegades_maksa=0
    else :  # ja kreklu summa ir mazāka par 50 euro, piegādas maksa ir True (par piegādi jāmaksā 15 euro)
        piegade=True
        piegades_maksa=15
    
    if piegade==True:  # ja piegāde ir True, piegādes cenu pieskaita pie pasūtījuma summas. ja piegāde nav True, pasūtījuma summa ir vienāda ar kreklu summu
        summa=kreklu_summa+15
    else :  
        summa=kreklu_summa

    return kreklu_summa, summa, piegades_maksa  # atgriež vērtības, kuras vēlāk vajadzēs izprintēt čekā
    
print("Sveiki! Prieks Jūs redzēt. Sāksim veidot pasūtījumu.")
print("Ja pasūtījuma summa pārsniedz 50€, piegāde par brīvu!")
print("(Piegādes cena 15€)")
while True :  # kamēr lietotājs ievada datus, programma turpina darbu
    kreklu_daudzums = int(input("Cik daudz kreklu Jūs vēlaties pasūtīt? "))
    if kreklu_daudzums<0:  # ja kreklu daudzums ir negatīvs, programma paziņo, ka ievadītais daudzums ir nepareizs un jautā ievadīt to atkal
        print("Ievadiet pareizu kreklu daudzumu.")
        continue
    else :  # ja kreklu daudzums ir pozitīvs, programma turpina tālāk
        while True :  # kamēr lietotājs ievada datus, programma turpina darbu
            apdrukas_veids = str(input("Kāda veida apdruku Jūs vēlaties? (TEKSTS (5€), ZIME (7€), FOTO (10€)) "))
            if apdrukas_veids=="TEKSTS" or apdrukas_veids=="ZIME" or apdrukas_veids=="FOTO" : # ja apdrukas veids ir pareizi ievadīts, programma izsit čeku un atvadās, beidzot darbu
                print()
                print("----------Čeks----------")
                print("Kreklu daudzums :", kreklu_daudzums)
                print()
                print("Apdrukas veids :", apdrukas_veids)
                print()
                print("Kreklu izmaksas :", pasuti_tkreklus(kreklu_daudzums, apdrukas_veids, True)[0],"€")
                print()
                print("Piegādes izmaksas :",pasuti_tkreklus(kreklu_daudzums, apdrukas_veids, True)[2],"€")
                print("- - - - - - - - - - - -")
                print("Kopējā summa :", pasuti_tkreklus(kreklu_daudzums, apdrukas_veids, True)[1],"€")
                print("------------------------")
                print()
                exit("Paldies, ka izmantojāt mūsu programmu, Jūsu krekli pie jums būs pēc 3-5 dienām.")
            else :  # ja apdrukas veids ir ievadīts nepareizi, programma to paziņo un liek ievadīt to atkal
                print("Ievadiet pareizu apdrukas veidu.")
                continue
