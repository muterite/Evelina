name = "Anna" #teksts var būt ar garumzīmēm, mainīgos bez garumzīmēm un pēdiņām
teksts = "teksts"
skaitlis = 9 #skaitliskā vērtība nekad nav pēdiņas
print(name)
kombo = name, teksts
print(kombo)
#atrast vārda garumu
varda_garums = len(name)
print(varda_garums)
#chained_assingment = kaskādes veida piešķiršana :
a = b = c = 300
print(a, b, c)

a, b = 10, "hello"
print(a)
print(b)

masina = "Volvo"
x = 50
x, y = 5, 10
print(x+y)
z = x+y
print(z)
