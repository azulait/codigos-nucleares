
hp1=50
hp2=50
turno=0

while hp1>0 and hp2>0:
    if turno % 2==0:
        import random
        atk=random.randint(2,10)
        hp2-=atk
        print(f"riuk hizo un ataque de {atk} , a ken le quedan {hp2} de vida")
    else:
        import random
        atk=random.randint(2,10)
        hp1-=atk
        print(f"ken hizo un ataque de {atk} , a riuk le quedan {hp1} de vida")
    turno+=1

if hp1>hp2:
    print("el ganador es riuk")
else:
    print("el ganador es ken")


