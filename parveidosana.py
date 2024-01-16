# int pārveidošana uz str(a un b saskaita)
# a un b kā teksts tiek konkatenēti(concat)
a, b = 5, 7
print("skaitlis", a+b) #int tipa mainīgie tiek saskaitīti
print("teksts", str(a)+str(b))
a = str(a)
b = str(b)   #var arī šādi (nav iekšā "print")
print(a+b)

#str pārveidošana uz int
s = "123"
t = "456"
print(s+t, type(s+t))
a = int(s)   # s ciparu virkni pārveido par skaitli (inttipa mainīgo) 
b = int(t)
print(a+b, type(a+b))

# pārveido no int uz float un tad atpakaļ uz int
x = 5
print(x, type(x))   
x = float(x)         # pārveido uz float
print(x, type(x)) 
x = int(x)           # atpakaļ uz int
print(x, type(x))

a = 123.4
a = int(a)
print(a, type(a))
