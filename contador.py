palabra=input("diga la palabra ")
caract=0
vocal=0
cons=0
for i in str (palabra):
    caract+=1
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        vocal+=1
    elif i!= " ":
        cons+=1

print(caract)
print(f"vocales= {vocal} \n consonantes={cons}")