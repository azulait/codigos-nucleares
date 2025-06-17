productos=[
    {"nombre": "ma", "precio": 100},
    {"nombre": "pa", "precio": 200}
]

def agregar():
    prod=input("agregar artuclo")
    prec=int(input("ingrese precio"))
    productos.append({"nombre":prod, "precio":prec })


def borrar():
    for i in productos:
        print(i["nombre"])
    borra=input("que item desea borrar")
    productos.pop()

while True:
    op=int(input('''
                 1-agregar
                 2-borrar
                 3-actualizar
                 4-mostrar
                 5-salir'''))
    match op:
        case 1:
            agregar()
        case 2:
            borrar()
        case 3:
            for n, produ in enumerate(productos):
                print(n+1, produ["nombre"], "$", produ["precio"])
            actualizar=(input("que producto desea modificar"))
            if actualizar==productos["nombre"]:
                actualizarprecio=int(input("indique nuevo precio de ", actualizar))
                productos["precio"]=actualizarprecio
        case 4:
            for n, produ in enumerate(productos):
                print(n+1, produ["nombre"], "$",produ["precio"])
                