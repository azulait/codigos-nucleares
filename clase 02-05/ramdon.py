import random, time
meta=30
j1=0
j2=0
turno=1
while j1<meta and j2<meta:
    
    if turno % 2==0:
        print("turno de jugador 1")
        dado=random.randint(1,6)
        j1+=dado
        time.sleep(2)
        print(f"el jugador 1 saco un {dado} \nel jugador 1 lleva {j1}")
        turno+=1
    elif turno % 2!=0:
        print("turno de jugador 2")
        dado=random.randint(1,6)
        j2+=dado
        time.sleep(2)
        print(f"el jugador 2 saco un {dado} \nel jugador 2 lleva {j2}")
        turno+=1

if j1>j2:
    print("el ganador es el jugador 1")
else:
    print("el ganadir es jugador 2")

