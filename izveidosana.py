# ar inicializācijas virkni
# key:value ir pāris
dd = {"četri":(4, "four"), "divi":(2, "two"), "trīs":(3, "three")}
print(dd)  # izdrukā vārdnīcu
print(len(dd))  # atgriež vārdnīcas garumu
print(",".join(dd.keys()))  #atgriež atslēgas


#fromkeys metode
vertiba = input("Ievadi key: ")
dati = ("viens", "divi", 'trīs')
vardnica = dict.fromkeys(dati, vertiba)
print(vardnica)