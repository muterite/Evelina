C = 1
x = int(input("Ievadi pirmo skaitli :\n"))
y = int(input("Ievadi otro skaitli :\n"))
if x>y :
    A=x
    B=y
elif x<y :
    A=y
    B=x
while C > 0 :
    C = A%B
    if C > 0 :
        A=B
        B=C
        continue
    else :
        print(B)
