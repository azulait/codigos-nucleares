caja1=30
caja2=30
caja3=30
clave1=123
clave2=456
clave3=789
intentos=3
user1="azulait"
user2="javi"
user3="mati"
saldo1=150000
saldo2=150000
saldo3=150000

usuario=str(input("ingrese su usuario"))
pas=int(input("ingrese su clave"))

if usuario==user1:
    while pas!=clave1 and pas!=clave2 and pas!=clave3:
        intentos-=1
        pas=int(input("intente nuevamente su clave"))
    
    print("bienvenido al sistema ", user1 , "\ntu saldo es de ", saldo1 )
    dinero=int(input("cuanto dinero desea sacar \nsolo multiplos de 5000"))



