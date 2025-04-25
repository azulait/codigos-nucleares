print("bienvenido a walmart \n que le gustaria llevar? \n ")
total=0
res=0
while res!=2:
    prod=int(input("1-leche $1.500 \n 2-huevos 12u $3.700 \n 3-pan molde $3.000 \n 4-cereal $2.500 \n "))
    if prod==1:
        cant=int(input("cuantos desea llevar?"))
        total+=1500*cant

    elif prod==2:
        cant=int(input("cuantos desea llevar?"))
        total+=3700*cant

    elif prod==3:
        cant=int(input("cuantos desea llevar?"))
        total+=3000*cant

    elif prod==4:
        cant=int(input("cuantos desea llevar?"))
        total+=2500*cant
    print("su total es ", total)
    res=int(input("desea agregar mas productos? \n 1-si \n 2-no \n"))

print("su total a pagar es ", total)
