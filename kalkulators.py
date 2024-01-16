a = int(input("a= "))
b = int(input("b= "))
darbiba = input("sask/atn/reiz/dal:")
if darbiba == "sask" :
    c = a+b
elif darbiba == "atn" :
    c = a-b
elif darbiba == "reiz" :
    c = a*b
elif darbiba == "dal" :
    c=a/b
else :
    print("nepareizi ievadīta darbība")
print("Atbilde ir",c)