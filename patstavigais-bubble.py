def burbulis(saraksts):
    elementi = len(saraksts)
    for i in range(elementi):
        for j in range(0, elementi-i-1):
            if saraksts["rezultats"[j]]>saraksts["rezultats"[j+1]]:
                saraksts[j], saraksts[j+1] = saraksts[j+1], saraksts[j]

def datu_iegusana():
    dati = {"vards":[], "rezultats":[]}
    dati["vards"] = []
    dati["rezultats"] = []
    skaits = int(input("Cik studentu rezultātus Jūs vēlaties ievadīt?\n"))
    for i in range(skaits):
        vards=str(input(f"Ievadiet {i+1}. studenta vārdu:\n"))
        rezultats=int(input("Ievadiet studenta iegūto rezulātu pilnos punktos(0-100p):\n"))
        print()
    dati.update({vards:rezultats})

   # burbulis(dati["rezultats"])
   # print("Sakārtotais saraksts:")
    for i in range(dati["rezultats"]):
        print(dati[i], end="\n" )
    
datu_iegusana()
    

