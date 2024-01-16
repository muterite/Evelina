menesis = str(input("Ievadi mēnesi (janvāris/februāris/marts/aprīlis/maijs/jūnijs/jūlijs/augusts/septembris/oktobris/novembrirs/decembris):"))
if menesis in ("janvāris","marts", "maijs", "jūlijs", "augusts", "oktobris", "decembris") :   # ja ir ievadīts kāds no šiem mēnešiem, dienas ir 31
    dienas = "31 diena"
elif menesis == "februāris" :   # ja ir ievadīts februāris, ir 28 dienas
    dienas = "28 dienas"
elif menesis in ("aprīlis", "jūnijs", "septembris", "novembris") :   # ja ir ievadīts kāds no šiem mēnešiem, tad ir 30 dienas
    dienas = "30 dienas"
print(menesis, ":", dienas)

