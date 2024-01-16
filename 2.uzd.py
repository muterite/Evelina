skaitli = {}
for i in range(5) :
    atslega = input("Ievadi skaitli: ")
    elements = input("Uzraksti šo skaitli ar vārdiem: ")
    skaitli.update({atslega:elements})
print(skaitli)

for atslega in sorted(skaitli, reverse=True):
    print(atslega,skaitli[atslega])

print("-----------------")

kartots=sorted(skaitli,key=skaitli.get)
for vertiba in kartots:
    print(vertiba,skaitli[vertiba])