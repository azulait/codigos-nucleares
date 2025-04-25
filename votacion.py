votantes=int(input("ingrese cuantos votantes hay "))

mario=0
luigi=0
nulo=0

for i in range(votantes):
    voto=int(input("por quien desea votar: \n 1-Mario \n 2-Luigi \n"))
    if voto==1:
        mario+=1
    elif voto==2:
        luigi+=1
    else:
        nulo+=1

print(f"mario consiguio {mario} votos \n luigi consigio {luigi} votos \n votos nulos= {nulo}")

if mario>luigi:
    print("el ganador es el hermano mayor con un ", round((mario)*100/(votantes-nulo),2) , "% de los votos")
elif luigi>mario:
    print("el ganador es el mario verde con un ", round((luigi)*100/(votantes-nulo),2) , "% de los votos")
else:
    print("tenemos un empate")


