print('Sākas programma')

def sveiks(vards):
    print('Labrīt,', vards)
    print('Prieks Tevi redzēt!')
    print('Cerams Tev ir laba diena!')

sveiks("Pēteri!")
sveiks("Jāni!")
sveiks("Anna!")

platums, augstums = 5, 7
laukums = platums * augstums

def lauk(num1, num2):
    return num1*num2
laukums = lauk(5,7)
print(laukums)