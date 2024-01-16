file_name = "dzest.txt"
add_me_1 = "Drīz būs Ziemassvētku brīvdienas!"
add_me_2 = "Karstais dzēriens ir bomba!"

try:
    with open(file_name, "a", encoding="UTF=8") as fails:
        fails.write("\n"+ add_me_1)
        fails.write("\n"+ add_me_2)
except FileNotFoundError :
    print("Kļūda: fails", file_name, "nav atrasts.")
except Exception as e:
    print("Kļūda: Neparedzēta kļūda -", e)