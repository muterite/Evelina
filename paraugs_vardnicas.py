krasas = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for atslega in sorted(krasas):  # sakārtot pēc atslēgas augošā secībā
    print(atslega, krasas[atslega])

veikals = {
    'banāni':12,
    'apelsīni':32,
    'arbūzi':21,
    'mandarīni':17,
    'vīnogas':15
}


array = []
for x in veikals:
    array.append([veikals[x],x])
print(array)
print(sorted(array))


kartots=sorted(veikals,key=veikals.get)
for vertiba in kartots:
    print(vertiba,veikals[vertiba])


kartots = sorted(veikals,key=veikals.get)
kartota_vardnica = {}

for key in kartots:
    kartota_vardnica[key] = veikals[key]
print(kartota_vardnica)


