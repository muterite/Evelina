x = int(input("Ievadīt skaitli :"))
if 0<= x <=100 :
    if x>=90 :
        print("Balles : 9")
    elif x>=70 :
        print("Balles : 7")
    elif x>=40 :
        print("Balles : 4")
    else :
        print("Tests nav nokārtots. :(")
else :
    print("Ievadi citu skaitli")
