for i in range(1,13):
    print("Cik ir", i, "x 7?")
    reiz=7
    atbilde = input()
    if atbilde == "stop" :
        break
    if atbilde == "izlaist" :
        print("piemērs izlaists")
        continue
    pareizi = i*reiz
    if int(atbilde) == pareizi :
        print("Atbilde pareiza")
    else :
        print("Atbilde nepareiza")