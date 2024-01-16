kontakti = {"vards": [], "numurs":[]}  
kontakti["vards"] = ["Madara", "Līga", "Marta", "Krišjānis"]
kontakti["numurs"] = ["22002982", "28449306", "21906672", "26405512"]

   

while True: 
    print("Sveiki, ko vēlaties darīt?")
    print("1 - drukāt esošos kontaktus")
    print("2 - pievienot kontaktu")
    print("3 - izdzēst kontaktu")
    print("4 - iziet no programmas")
    izvele = int(input())
    if izvele == 1:
        print("Jūs izvēlējātis taustiņu 1 - jūsu kontakti ir uz ekrāna")
        print(kontakti["vards"], kontakti["numurs"])
        print("-----------------------")
    elif izvele == 2:
        print("Jūs izvēlējātis taustiņu 2 - pievienot jaunu kontaktu")
        vards = input("Ievadi vārdu: ")
        numurs = input("Ievadi numuru: ")
        kontakti.update({vards:numurs})
        print(kontakti)
        print("-----------------------")
    elif izvele == 3:
        print("Jūs izvēlējātis taustiņu 3 - izdzēst kontaktu")
        vards = input("Ievadi vārdu: ")
        kontakti.pop(vards)
        print(kontakti)
        print("-----------------------")
    else:
        print("Jūs izvēlējātis taustiņu 4 - iziet no programmas")
        print("Paldies, ka bijāt ar mums!")
        exit()