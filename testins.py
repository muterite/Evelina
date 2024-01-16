fails = open("ziema.txt", "w", encoding="UTF-8")  # izveido neeksistējošu failu no jauna
# ieraksta failā datus
saraksts = ["Alūksne\n", "Valmiera\n", "Balvi\n"]  
fails.writelines(saraksts)  # ieraksta vairākas rindiņas
fails.write("Es ar nepacietību gaidu pusdienas.")
fails.close()

# pārrakstīt faila saturu
fails = open("ziema_copy.txt", "w+", encoding="UTF-8")
fails.write("Varētu drīz iet pusdienās!")
# parāda faila saturu 
fails = open("ziema_copy.txt", "w+", encoding="UTF-8")
print(fails.read())
fails.close

fails = open("ziema_copy.txt", "a+", encoding="UTF-8")
fails.write("\nCerams pusdienas šodien būs garšīgas!")