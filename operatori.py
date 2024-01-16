x = int(input("Ievadi 1. skaitli: "))
y = int(input("Ievadi 2. skaitli: "))
z = int(input("Ievadi 3. skaitli: "))

# loģiskais and

if x>0 and y>0 and z>0 :
    print("Visi skaitļi lielāki par 0")
else :
    print("Vismaz viens skaitlis ir mazāks vai vienāds ar 0")

# loģiskais or

if x==5 or y==5 or z==5 :
    print("Vismaz viens no ievadītajiem skaitļiem ir 5")
else :
    print("Neviens no ievadītajiem skaitļiem nav 5")