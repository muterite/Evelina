import math

print("Sveiks, Andri! Sākam darbu.")

veikals = input("Uz kuru veikalu Tu dosies pirkt materiālus? ")
cena = float(input("Ievadi linoleja cenu (€/m2): "))
rulla_platums = float(input("Ievadi ruļļa platumu (m): "))
telpa = float(input("Ievadi telpas platību (m2): "))
apaksklajs = input("Vai klients vēlas ieklāt apakšklāju? (jā/nē): ")
if apaksklajs == "jā" :
    apaksklaja_cena = float(input("Ievadi apakšklāja cenu (€/m2): "))
rulla_garums = math.ceil(telpa/rulla_platums)
nopirkts = rulla_garums*rulla_platums

print()
print("--------------",veikals,"----------------")
print()
print("Telpai vajadzēs", telpa, "m2 linoleja")
print()
print("--------------------------------------")
print()
print("Jūsu izvēlētais linolejs maksā", cena, "€")
print("Izmaksa par linoleju:", cena*nopirkts, "€")
print("Nopirktais linolejs:", nopirkts, "m2")
print()
print("--------------------------------------")
print()
print("Pāri palikušais linolejs:", round(nopirkts-telpa, 2), "m2")
print()
print("--------------------------------------")
if apaksklajs == "jā" :
    print()
    print("Izmaksa par apakšklāju:", round(apaksklaja_cena*math.ceil(telpa), 2), "€")
    print()
    print("--------------------------------------")
