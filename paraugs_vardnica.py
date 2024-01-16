# izveidot vārdnīcu ar skaitļa tipa atslēgām

dict1 = {
    1: "Tev",
    2: "garšo",
    3: "āboli"
}
print("Vārdnīca ar skaitļa tipa atslēgām:")
print(dict1[1])
print(dict1[2])
print(dict1[3])

#izveido vārdnīcu ar non-numeric keys

dict2 = {
    "Auglis":"ābols",
    "Augļu karalis":"Mango",
    "Sezonas auglis":"Apelsīns"
}
print("Vārdnīca ar non-numeric keys")
print(dict2["Auglis"])
print(dict2["Augļu karalis"])
print(dict2["Sezonas auglis"])