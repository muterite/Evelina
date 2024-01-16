sast_saraksts = []
sast_cenas = []
sast_daudzumi = []
kopsumma = 0

print("Sveika, omīt!")
cik_sast = int(input("Cik sastāvdaļas būs nepieciešamas? "))

for i in range(0, cik_sast):
    sastavdala = input("Kas ir sastāvdaļa, ko vajag receptes pagatavošanai? ")
    s_cena = float(input("Cik maksā šī sastāvdaļa?(€/kg) "))
    s_daudz = int(input("Cik daudz šīs sastāvdaļas vajag receptes pagatavošanai?(g) "))
    sast_saraksts.append(sastavdala)
    sast_cenas.append(s_cena)
    sast_daudzumi.append(s_daudz)

ievarijuma_daudz = int(input("Cik reizes vēlaties taisīt recepti?"))

#for i in range(1, len(sast_saraksts)+1) :
#    x = 1
#    majas_ir = input("Vai jums mājās jau ir", sast_saraksts[x], "?(jā/nē)")
#    if majas_ir == "jā" :
#        majas_cik = float("Cik daudz", sast_saraksts[x], "jums ir?(g)")
#    else :
#        continue
#    x=+1

print("Dosimies uz veikalu nopirkt vajadzīgās preces.")
for i in range(1, len(sast_saraksts[i])+1):
    for y in sast_cenas :
        for h in sast_daudzumi :
            summa = y*h
            kopsumma = kopsumma + summa
            print("Par", sast_saraksts, "iztērēji :", summa)
    


