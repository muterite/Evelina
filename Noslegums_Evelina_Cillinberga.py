from datetime import datetime   # importē datetime priekš pašreizējā laika noteikšanas

now = datetime.now() # mainīgajā saglabā pašreizējo laiku un datumu

def iegut_datus() :    # funkcija uzdod lietotājam jautājumus attiecībā uz ievades datiem, lietotājs tos ievada
    experiment_name = str(input("Ievadi eksperimenta nosaukumu :\n"))
    if experiment_name == "exit" or experiment_name == "stop" or experiment_name == "iziet" :
        quit()
    time = now.strftime("%m/%d/%Y, %H:%M:%S")
    if time == "exit" or time == "stop" or time == "iziet" :  # ja mainīgais ir kāds no izejvārdiem (stop, iziet, exit), tad programma beidz darbību (attiecas uz visiem turpmākaliem šāda veida if statementiem)
        quit()
    user_name = str(input("Ievadi savu vārdu :\n"))  # title pārveido vārda pirmo burtu par lielo burtu
    user_name = user_name.replace(" ", "")  # "izdzēš" atstarpes
    user_name = user_name.capitalize() # nomaina pirmo burtu uz lielo burtu
    if user_name == "exit" or user_name == "stop" or user_name == "iziet" :
        quit()
    place = str(input("Ievadi eksperimenta veikšanas vietu :\n"))
    if place == "exit" or place == "stop" or place == "iziet" :
        quit()
    # iegūtos datus ieliek sarakstā un globalizē tālākai izmantošanai
    global values_list  
    values_list = [experiment_name, time, user_name, place]

def saglabat_datus() :  # funkcija atver un ieraksta datus eksistējošajā failā "eksperimenta_dati.txt"
    try :
        file = open("eksperimenta_dati.txt", "a", encoding="UTF-8")
        file.writelines("Eksperimenta nosaukums : " + values_list[0] +"\nDatums un laiks : "+ values_list[1]+ "\nAutors : "+ values_list[2]+ "\nEksperimenta veikšanas vieta : "+ values_list[3] + "\n---------\n")
    except FileNotFoundError :  # parāda kļūdu, ja fails neeksistē vai nav atrasts
        print(f"Kļūda: Fails eksperimenta_dati.txt nav atrasts")
    except Exception as e :  # parāda kļūdu, ja rodas citas problēmas ar failu
       print("Kļūda: neparedzēta kļūda -", e)

def galvena() :  # funkcija izsauc pirmās divas funkcijas secīgi
    print(f"Esi sveicināts programmā DataDate !")
    print("Programmas mērķis ir Tev atvieglot eksperimentu datu ievadi.")
    print("----------")
    iegut_datus()
    saglabat_datus()
    # tiek globalizēts "answer" lai to vēlāk izmantotu while ciklā
    global answer 
    answer = str(input("Vai vēlaties ievadīt citus datus?(j/n)\n"))
    if answer == "exit" or answer == "stop" or answer == "iziet" :
        quit()

galvena()
while answer == "j" : # kamēr lietotājs vēlas ievadīt vēl eksperimenta datus, programma turpina darbību un jautā ievadīt datus atkal
    iegut_datus()
    saglabat_datus()
    answer = str(input("Vai vēlaties ievadīt citus datus?(j/n)\n"))