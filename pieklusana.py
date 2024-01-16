#izveidot vārdnīcu, kas satur sarakstu
valstis = {
    'Somija':['Helsinki','Rovaniemi','Tampere','Kemijarvi','Jyvaskyle'],
    'Norvēģija':['Oslo','Bergena','Arendāla','Trumse','Molde'],
    'Dānija':['Kopenhāgena','Odense','Esbjerga','Aarhus','Ronne']
}
# 1. variants ar for ciklu
for atslega, vertiba in valstis.items():
    for i in vertiba:
        print("{}: {}".format(atslega,i))
    print("--------------------")

# 2. variants ar for ciklu vienai atslēgu grupai
for i in valstis['Dānija']:
    print(i)

# iegūt konkrētās pilsētas no vārdnīcas
print(valstis["Somija"][:3])

# iegūt pēdējās 2 pilsētas
print(valstis["Norvēģija"][-2:])

# iegū 2o līdz 5to pils
print(valstis["Dānija"][1:5])