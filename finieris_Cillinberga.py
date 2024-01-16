print("Sveiki! Šī programma palīdzēs jums uzzināt jūsu pasūtījuma izdevumus, kā arī pasūtījuma specifikācijas. Sākam darbu!")
print()

atbilde = "jā"
finiera_kopsumma = 0
lenkv_stipr_kopsumma = 0
sturu_kopsumma = 0
virsmas_kopsumma = 0
kopskaits = 0

while atbilde == "jā" :
    lenkv_liste_cena = float(input("Ievadi vienas leņķveida līstes cenu: "))
    sturu_cena = float(input("Ievadi viena stūra savienojuma cenu: "))
    garums = float(input("Ievadi podesta garumu(cm): "))
    platums = float(input("Ievadi podesta platumu(cm): "))
    augstums = float(input("Ievadi podesta augstumu(cm): "))
    skaits = int(input("Ievadi šādu podestu skaitu: "))

    skaldne1_4 = garums*augstums
    skaldne2_5 = garums*augstums
    skaldne3_6 = platums*augstums
    virsma = skaldne1_4*2 + skaldne2_5*2 + skaldne3_6*2
    vajadzigais_finieris = virsma*skaits
    vajadzigie_lenkv_stipr = 12*skaits
    vajadzigie_sturi = 8*skaits


    mat = input("Ievadi finiera materiālu(bērzs/egle/priede): ")
    if mat == "bērzs" :
        finiera_izmaksa_m2 = 24.60
    elif mat == "egle" :
        finiera_izmaksa_m2 = 31.04
    elif mat == "priede" :
        finiera_izmaksa_m2 = 31.74


    finiera_summa = (vajadzigais_finieris/10000)*finiera_izmaksa_m2
    lenkv_stipr_summa = vajadzigie_lenkv_stipr*lenkv_liste_cena
    sturu_summa = vajadzigie_sturi*sturu_cena

    finiera_kopsumma = finiera_kopsumma+finiera_summa
    lenkv_stipr_kopsumma = lenkv_stipr_kopsumma+lenkv_stipr_summa
    sturu_kopsumma = sturu_kopsumma+sturu_summa
    virsmas_kopsumma = virsmas_kopsumma+virsma
    kopskaits = kopskaits+skaits

    print()
    print()
    print("------------------------------")
    print("Izvēlētā podesta parametri: ", garums, "cm x", platums, "cm x", augstums, "cm")
    print("Podestu daudzums: ", skaits)
    print("Finiera virsmas laukums : ", virsma, "cm2 = ", virsma/10000, "m2")
    print("Finiera izmaksas :", round(finiera_summa, 2), "€")
    print("Pārējo detaļu izmaksas: ", round(sturu_summa+lenkv_stipr_summa, 2), "€")
    print()

    atbilde = input("Vai vēlaties pasūtīt vēl podestus?")

else :
    print()
    print()
    print("------------------------------")
    print("Kopā iztērētias finieris:", virsmas_kopsumma, "cm2 = ", virsmas_kopsumma/10000, "m2")
    print("Kopējie izdevumi par finieri: ", round(finiera_kopsumma, 2), "€")
    print("Kopējie izdevumi par stūra savienojumiem: ", round(sturu_kopsumma, 2), "€")
    print("Kopējie izdevumi par leņķveida līstēm: ", round(lenkv_stipr_kopsumma, 2), "€")
    print("Izveidoto podestu skaits: ", kopskaits)