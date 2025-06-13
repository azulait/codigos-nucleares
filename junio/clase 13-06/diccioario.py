frutas={
    "manzana": 1500,
    "pera": 1200,
    "piña": 2000
}
def infrutas():
    fruta=input("que fruta desea agregar")
    precio=int(input("a que precio"))
    frutas[fruta]=precio

def comprar():
    total=0
    while True:
        cont=1
        for fruta , precio in frutas.items():
            print(cont,"-", fruta, precio)
            cont+=1
        op=(input("elija que fruta quiere llevar" \
        "0 para salir"))
        cant=(int(input("cuantos k")))
        total=frutas[op]*cant
        print("serian  $", total)
        if op=="0":
            break

while True:
    op=int(input('''elija
                 1-ingresar fruta y precio
                 2-actualizar precio
                 3-borrar fruta y precio
                 4-mostrar todas las frutas y precios
                 5-comprar
                 6-salir
                 '''))
    match op:
        case 1:
            infrutas()
        case 2:
            cont=1
            for fruta , precio in frutas.items():
                print(cont,"-", fruta, precio)
                cont+=1
            numfruta=(int(input("seleccione la fruta quiere actualizar")))
            preciomod=int(input("ponga el nuevo precio"))
            frutas[numfruta-1]=preciomod
        case 3:
            cont=1
            for fruta , precio in frutas.items():
                print(cont,"-", fruta, precio)
                cont+=1
            delfruta=(input("elija que fruta quiere eliminar"))
            del frutas[delfruta]
        case 4:
            cont=1
            for fruta , precio in frutas.items():
                print(cont,"-", fruta, precio)
                cont+=1
        case 5:
            comprar()
        case 6:
            print("hasta luego")
            break