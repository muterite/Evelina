import math
import random
print("Ievadiet riņķa līnijas rādiusu: ")
radiuss = float(input())
print(radiuss)
print("Riņķa līnijas garums: ", "%.2f"%(2*math.pi*radiuss))
print("Riņķa līnijas laukums: ", "%.2f"%(math.pi*math.pow(radiuss, 2)))
print("Ievadiet taisnleņķa trijstūra pirmās katetes garumu:")
katete_1 = float(input())
print("Ievadiet taisnleņķa trijstūra otrās katetes garumu:")
katete_2 = float(input())
print("Taisnleņķa trijstūra hipotenūzas garums: ", "%.2f"%(math.sqrt(math.pow(katete_1, 2)+math.pow(katete_2, 2))))
randoms = random.randint(1, 10)
print("Gadījuma skaitlis no 1 līdz 10: ", randoms)