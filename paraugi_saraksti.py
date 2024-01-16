#uzrakstīt programmu, kurā ir 2 saraksti. Ar + abus apvienot
mans_saraksts = ["svece", 2, "sāls"]   # pirmais elements ir ar indeksu 0
tavs_saraksts = ["karstmaize", "braunijs", "kafija"]

liels_saraksts = mans_saraksts + tavs_saraksts
print(liels_saraksts)

# nokopēt saraksta vērtības un ielikt tās jaunā sarakstā
milzis = ["dzērvene", "zupa", "tastatūra"]
jauns = list(milzis)   # list ir atslēgvārds, kas nokopē visu sarakstu
print(jauns)

# izveidot sarakstu ar 4 krāsu nosaukumiem. Atrast katra elementa garumu
krasas = ["dzeltens", "sarkans", "zils", "zaļš"]
tukss = []    # tukšs saraksts
for krasa in krasas :
    burti = 0   # katru reizi palaižot programmu/sarkstu, atgriežas uz 0
    for burts in krasa :
        burti +=1   # katru reizi pieskaita 1
    pagS =[krasa, burti]
    tukss.append(pagS)
print(tukss)

# kā šo kodu var uzrakstītar mazāk rindiņām? vai ir vienkāršāks veids kā atrast vārda garumu?
krasas = ["dzeltens", "sarkans", "zils", "zaļš"]
for krasa in krasas :
    print(len(krasa), end=" ")   # len izskaita burtus kādā vārdā

# vel viens variants
krasas = ["dzeltens", "sarkans", "zils", "zaļš"]
jauns = []
for krasa in krasas :
    jauns.append([krasa, len(krasa)])
    print(jauns)