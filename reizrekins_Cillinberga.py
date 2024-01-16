x = int(input("Ievadi skaitli :"))
skaitli = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for rez in skaitli :   # katru skaitli no saraksta "skaitli" ņem pēc kārtas un izpilda lejā norādīto funkciju print
    print(x, "x", rez, "=", rez*x)