import random  #random izvēlas skaitļus, mūsu gadījumā gājienus
gajieni = ["akmens","papīrs","šķēres"]

cilveka_gajiens = input("Akmens, šķēres vai papīrs? :")
datora_gajiens = random.choice(gajieni)  #dators uz random izvēlēsies gājienu

print(f"Cilveks: {cilveka_gajiens} VS Dators: {datora_gajiens}")  # tas "f" figūriekavās esošo uztver kā mainīgu, lai nav jāliek daudz komati un pēdiņas
if cilveka_gajiens == datora_gajiens :
    print("Neizšķirts")
elif cilveka_gajiens == "akmens" and datora_gajiens == "šķēres" :
    print("Tu uzvarēji :D")
elif cilveka_gajiens == "papīrs" and datora_gajiens == "akmens" :
    print("Tu uzvarēji :D")
elif cilveka_gajiens == "šķēres" and datora_gajiens == "papīrs" :
    print("Tu uzvarēji :D")
else :
    print("Tu zaudēji :(")