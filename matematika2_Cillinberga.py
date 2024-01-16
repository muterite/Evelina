print("Divciparu skaitļa ciparu summas aprēķins")
print("Ievadiet divciparu skaitli!")
skaitlis = int(input())   # šeit lietotājs ievada skaitli, "int" norāda, ka ievadītā informācija būs vesels skaitlis
print("Divciparu skaitlis =", skaitlis)
cipars1 = skaitlis//10  # iegūst pirmo ciparu dalot ar 10, taču obligāti jāiegūst viens cipars, tādēļ dalīšanu veic ar atlikumu to nerādot, izmantojot "//"
cipars2 = skaitlis%10   # iegūst otro ciparu dalot ar 10, taču šajā gadījumā vajag tikai atlikumu, tādēļ izmanto "%"
print("Pirmais cipars:", cipars1)
print("Otrais cipars:", cipars2)
print(cipars1 + cipars2)