totalp=0
totalart=0
prod=0
def listprod():
    global totalp, totalart,prod,iva
    prod=int(input('''elija su producto:
          1.Leche $1.700
          2.Pan $3.000
          3.Huevos $8.700
          4.Jamon $2.500
         69.Salir 
                   '''))
    match prod:
        case 1:
            totalp+=1700
            totalart+=1
        case 2:
            totalp+=3000
            totalart+=1
        case 3:
            totalp+=8700
            totalart+=1
        case 4:
            totalp+=2500
            totalart+=1
        case 69:
            print("nos vemos")

        case _:
            print("opcion no valida")
    print("su total es $", totalp)
    iva=totalp*0.19

def boleta():
    print(f"gracias por su compra {nombre}, su precio neto es ${totalp} y su total a pagar mas iva es de ${totalp+iva} por una cantidad de {totalart} articulos")


nombre=str(input("ingrese su nombre"))
while True:
    op=int(input(f'''que desea hacer {nombre}:
                 1.comprar
                 2.boleta
                 3.salir '''))
    match op:
        case 1:
            while prod!=69:
                listprod()
        case 2:
            if totalp==0:
                print("usted no ha elegido ningun articulo")
            else:
                boleta()
        case 3:
            print("hasta luego, que le vaya bonito")
            break
            



