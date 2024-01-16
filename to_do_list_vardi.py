tasks = {}

print("Sveika Anna! :)")
print("Iespējamās darbības :")
print()
print("1 - Apskatīt darāmo darbu sarakstu")
print("2 - Pievienot darāmu darbu")
print("3 - Mainīt darba statusu")
print("4 - Uzstādīt darba termiņu")
print("5 - Sakārtot un apskatīt sarakstu pēc Tavas prioritātes (termiņš, darba statuss)")
print("6 - Eksportēt darāmos darbus teksta failā")
print()
print("Ko vēlies darīt?")
answer = int(input())

while True :
    if answer == 1 :
        for key, data in tasks.items():
            print(key, "-", data, )
    elif answer == 2 :
        print("Tu izvēlējies pievienot darāmu darbu")
        task = input("Kādu darāmo darbu vēlies pievienot?\n")
        completion = input("Vai darbs ir izdarīts? (j/n)\n")
        add = {task : completion}
        tasks |= add
        for key, data in tasks.items():
            print(key, "-", data, )
        
 #   elif answer == 3 :

#    elif answer == 4 :

 #   elif answer == 5 :

  #  elif answer == 6 :