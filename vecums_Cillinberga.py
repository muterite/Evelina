gadi = int(input("Ievadi suņa vecumu (pilnos gados) :"))
if gadi < 0 :    # funkcija pārbauda lai ievadītie gadi nav negatīvi, jo tas nav reāli
    print("Ievadi suņa vecumu vēlreiz")
elif gadi <= 2 :      # ja sunim ir mazāk par vai 2 gadi, tad izpildās dotais vienādojums
    vecums = gadi*10.5
else :    # ja suns vecāks par 2 gadiem, tad 
    vecums = (gadi-2)*4+21
print(vecums)