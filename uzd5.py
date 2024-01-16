def change() :
    gradi = float(input("Ievadi grādus pēc Celsija: "))
    far = "%.1f"%((gradi * (9/5)) + 32)
    print("Pārveidojot ", gradi, "°C ir ", far, "°F")
change()