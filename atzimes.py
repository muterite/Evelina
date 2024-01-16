# izveidot sarakstu "atzimes" ar punktiem (testā iegūtie)(10 rezultāti no 60-99)
# ar for ciklu 'iziet cauri' visam sarakstam
# ar elif nosacījumu uz ekrāna parādīt punktus un atzīmi
# >=90 - A; >=80 - B; 70-80 - C; 60-70 - D; zem 60 -F
# grūtāk - pielikt datu ievadi un atkarībā no ievadītā skaitļa, parādīt burtu

atzime = int(input("punkti : "))
#for atzime in punkti :
if atzime >=90 :
        rez = "A"
elif atzime >=80 :
        rez = "B"
elif atzime >=70 :
        rez = "C"
elif atzime >=60 :
        rez = "D"
else :
        rez = "F"
print(rez, atzime)


