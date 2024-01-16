name_and_username ={}
words = input("Ievadiet vārdu virkni: ")
words_split = words.split()
for word in words_split: 
    username = input(f"Lūdzu ievadiet lietotājvārdu priekš vārda '{word}' : ")
    name_and_username.update({word : username})
file_name = input("Ievadiet faila nosaukumu, kurā eksportēt datus: ")
file = open(file_name, "w", encoding="UTF-8")
file.writelines(f"Lietotājvārds: '{name_and_username[1]}'")
file.close()


