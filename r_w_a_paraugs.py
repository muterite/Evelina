failins = open("dati3.txt", "a", encoding="utf-8")

saraksts = ["Cēsis\n", "Valmiera\n", "Daugavpils\n"]
# failins.writelines(saraksts) # writelines, jo ar parasto write viņs visu sarakstu neuzrakstīs
failins.write("Šīs pilsētas ir interesantas :3\n")


# pārrakstīt faila saturu uz 3 valstīm
valstis = {"1":"Somija", "2":"Zviedrija", "3":"Norvēģija"}
failins = open("dati3.txt", "w", encoding="utf-8")
failins.writelines(str(valstis))