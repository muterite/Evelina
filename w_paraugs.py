fails = open("dati.txt", "a", encoding="utf-8")
fails.write("Ingvera sula garšo pēc sušī!\n")
# katru reizi palaižot programmu, teksts tiek pievienots klāt


fails = open("dati.txt", "r", encoding="utf-8")
print(fails.read())


fails = open("dati.txt", "w", encoding="utf-8")
# w pārraksta datus
fails.write("Mācos rakstīt failā\n")


fails = open("dati.txt", "a", encoding="utf-8") 
# a pievieno klāt datus esošajiem
fails.write("Ērces jau ir modušās! Kazas!!!")

fails.close()