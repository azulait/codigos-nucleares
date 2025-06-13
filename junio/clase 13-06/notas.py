notas=[55,66,23]
def agregarnotas():
        nota=int(input('ponga la nota que desea agregar'))
        notas.append(nota)
def borrarnotas():
        for i, nota in enumerate(notas):
              print(i+1, "-" , nota)
        bnota=int(input('seleccione la nota que desea borrar'))
        notas.pop(bnota-1)

while True:
    op=int(input('''eliga que desea hacer
                 1-ingresar nota
                 2-borrar nota
                 3-mostrar nota
                 4-sacar promedio
                 5-limpiar notas
                 6-salir
                 '''))
    match op:
        case 1:
            agregarnotas()
        case 2:
            borrarnotas()
        case 3:
            print(notas)
        case 4:
            totaln=0
            for nota in notas:
                 totaln+=nota
            prom=totaln/len(notas)
            print("el promedio es de ", prom)
        case 5:
            notas.clear()
            
        case 6:
            print("hasta la proxima")
            break
            



