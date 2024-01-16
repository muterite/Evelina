def teksts() :
    print("Sveiks!")
    print("Šeit ir pirmie horoskopu pareģojumi :\n")\
    
def teikumi() :
    for i in range(0, 12) :
        print("---------------")
        print(horoskopi[i])
        print("Sekojot līdzi apkārt notiekošjam, Tu gūsi vislabākās sekmes cilvēku iepazīšanā.")
        print("Tev šodien būs veiksmīga diena starp draugim, taču neveiksme būs sevis lutināšanā.")
        print("Atvēli laiku gan sev, gan citiem.")

atbilde = "jā"
horoskopi = ["Auns","Vērsis","Dvīņi","Vēzis","Lauva","Jaunava","Svari","Skorpions","Strēlnieks","Mežāzis","Ūdensvīrs","Zivs"]
rikojumi = ["Aizver acis un dziļi ieelpo, lai atbrīvotos no stresa.", "Dari kaut ko jaunu un izraujies no komforta zonas.","Iedod sev brīdi, lai baudītu iecienītu dziesmu vai grāmatu.", "Uzraksti sarakstu ar saviem sasniegumiem un sapņiem.", "Veic iedvesmojošu rītu rutīnu, lai uzlabotu dienas sākumu.", "Nestāvi pie savām domām - dari lietas, kas tevi priecē.", "Izvairies no pārmērīgas kofeīna vai salda ēdiena lietošanas.", "Nedēļas nogalē pievērs uzmanību savam iekšējam mieram.", "Pilnībā izbaudi katru ēdienu, baudot katra garšas niansi.", "Nedēļas laikā nodrošini sev kvalitatīvu atpūtu vismaz reizi.", "Novērtē svaigo gaisu un dabas skaistumu.", "Iekļauj diētā veselus ēdienus, kas veicina enerģiju.", "Atrodi laiku kādam hobijam vai aizraušanai.", "Nedēļas nogalē dodies pastaigā dabā.", "Izvairies no pārspīlētas darba slodzes.", "Pārtrauc uz laiku sociālo mediju lietošanu.","Iedod sev komplimentu."  ]

while atbilde == "jā" :
    teksts()
    teikumi()
    atbilde = input("\nVai vēlies nākamos pareģojumus?(jā/nē)")