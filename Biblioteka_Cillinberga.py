nenodoti_izdevumi = input("Vai personai ir nenodoti izdevumi?(jā/nē)")
if nenodoti_izdevumi == "jā" :   # ja ir nenodoti izdevumi, tad izdevumus nevar izsniegt
    print("Neizsniedzam izdevumus.")  
else :    # šeit ar else turpinās jautājumu virkne, lai uzzinātu dienu skaitu, jo izdevumus var izsniegt, jo nav nenodoti izdevumi 
    pieprasijums = input("Vai vajadzīgais izdevums ir pieprasīts?(jā/nē)")
    if pieprasijums == "jā" :   # ja izdevums ir pieprasīts, tad to dod uz 2 dienām (parādīts nākamajā rindā)
        print("Dodam izdevumu uz 2 dienām.")
    else :  # šeit turpinās jautājumu virkne, jo zinam, ka nav pieprasīts izdevums, tādēļ ir jāuzzin vairāk info
        zurnals = input("Vai tas ir žurnāls?(jā/nē)")
        if zurnals == "jā" :   # ja tas ir žurnāls, dod uz 7 dienām (parādīts nākamajā rindā)
            print("Dodam izdevumu uz 7 dienām.")
        else :  # jautājumu virkne turpinās, jo vēl jāuzzin, vai šo ne-žurnālu un nepieprasīto izdevumu ņems skolēns vai personāls
            kurs_nem = input("Izdevumu vajag skolēnam vai personālam?(skolēnam/personālam)")
            if kurs_nem == "skolēns" :   # ja izdevumu ņem skolēns, tad dod uz 14 dienām (parādīts nākamajā rindā)
                print("Dodam izdevumu uz 14 dienām.")
            else :   # ja izdevumu neņem skolēns, tad to ņem personāls, un to dod uz 28 dienām (parādīts nākamajā rindā)
                print("Dodam izdevumu uz 28 dienām.")

