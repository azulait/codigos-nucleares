num=1
total=0
par=0
imp=0
totalpr=0
totalipr=0
while num!=0:
    num=int(input("ingrese el numero que quiere sumar \n ingrese 0 para terminar \n "))
    total+=num
    if num % 2==0:
        totalpr+=num
        par+=1
    else:
        totalipr+=num
        imp+=1
print(f" el total es {total} \n el total de impares es {imp} y su suma fue de {totalipr} \n el total de pares fue {par} y su total fue {totalpr}")