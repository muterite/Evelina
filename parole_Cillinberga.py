pareizais_lietotajvards = "mazaisrakars"
pareiza_parole = 80085
meginajums = 1
atlikusie_meginajumi = 4

while meginajums<= 5 :     # kamēr mēģinājumu skaits nav vairāk par 5, programma turpinās, jautājot lietotājvārdu un paroli
    lietotajvards = input("Ievadi lietotājvārdu: ")
    parole = int(input("Ievadi paroli: "))
    if lietotajvards == pareizais_lietotajvards and parole == pareiza_parole :   # ja lietotājvārds un parole abi ir pareizi (tādēļ izmantoju "and"), tad pieslēgšanās ir veiksmīga un programma aptur "while" ciklu un dodas tālāk pie skaitļiem
        print("Pieslēgšanās veiksmīga!")
        break   # šeit ir iepriekš minētias break, kas aptur while cikla darbību un dodas pāri tam tālāk kodā
    elif lietotajvards == "stop" or parole == "stop" :  # ja lietotājvārds vai parole (tādēļ izmantots or) ir "stop", kas liecina ka lietotājs nevēlas turpināt, programma pasaka, ka tā beidzas un beidz darbību
        exit("Programmas beigas!")
    else :  # izmantoju else, jo, ja informācija ievadīta nepareizi, tad programma pasaka, ka dati ievadīti nepareizi un pasaka atlikušo mēģinājumu skaitu
        if meginajums==5 :  # ja mēģināts pieslēgties jau 5 reizes, tad programma to paziņo un beidz darbību 
            print("Atļauts mēģināt pieslēgties 5 reizes!")
            quit("Programmas beigas!")
        else :   # ja mēģināts pieslēgties mazāk kā 5 reizes, tad programma paziņo, ka dati ievadīti nepareizi, un cik mēģinājumi lietotājam ir palikuši
            print("Pieslēgšanās dati nepareizi, atlikuši", atlikusie_meginajumi, "mēģinājumi.")
            meginajums+=1
            atlikusie_meginajumi-=1

ciparu_skaits = 0
while (parole > 0):  # kamēr parole ir ievadīta (vismaz viens nenulles cipars), tad programma pārbauda un izdrukā no cik cipariem sastāv parole
    parole = parole//10
    ciparu_skaits = ciparu_skaits + 1
print("Ievadītās paroles garums: ", ciparu_skaits, "cipari")

sk1 = int(input("Ievadi pirmo veselo skaitli: "))
sk2 = int(input("Ievadi otro veselo skaitli: "))

if sk1>sk2 :  # ja pirmais skaitlis ir lielāks par otro (kas pēc noteikumiem nav pieņemams), tad programma pasaka lai ievada citus skaitļus un dod iespēju to izdarīt
    print("Ievadi citus skaitļus")
    sk1 = int(input("Ievadi pirmo veselo skaitli: "))
    sk2 = int(input("Ievadi otro veselo skaitli: "))

while sk1<0 or sk2<0 :  # kamēr pirmais vai otrais skaitlis ir negatīvi (pēc noteikumiem nav pieņemams), tikmēr programma pasaka lai ievada citus skaitļus un dod iespēju to izdarīt
    print("Ievadi citus skaitļus")
    sk1 = int(input("Ievadi pirmo veselo skaitli: "))
    sk2 = int(input("Ievadi otro veselo skaitli: "))

sum = 0
for i in range(sk1, sk2+1) : # šeit sākuma punkts ir pirmais skaitlis, kuru sākotnēji pieskaita gala summai, kas, palielinoties par 1 līdz otrajam skaitlim, tiek pieskaitīts summai un beidzas ar otrā ievadītā skaitļa pieskaitīšanu
    sum+=i
print("Summa :", sum)
