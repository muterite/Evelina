atbilde = input("Vai tev garšo piens?(j/n)")
if atbilde == "j" :  #salīdzināšanu veic ar 2 vienādības zīmēm
    print("Tu esi stiprs vīrs! Tā tik turpini.")


tests = input("Vai šodien ir jaungada diena?(j/n)")
if tests == "j" :
    print("Lauks salūtam!")
else:  #pie else nosacījuma nebūs (paliek pāri tikai 1 iespējamā atbilde)
    print("Bēdīgi...")  #šis tiek palaists tikai ja lietotājs neievada "j"