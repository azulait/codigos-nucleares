def cal_prom(s,d):
    return s/d


cantalumnos=int(input("ingrese la cantidad de alumnos: "))

promcurso=0
for a in range (1,cantalumnos+1):
    cantnotas=int(input("ingrese la cantidad de notas del alumno ", a , ": "))
    prom=0
    notaf=0
    for n in range (1,cantnotas+1):
        nota=int(input(f"ingrese la nota {n} del alumno {a}: "))
        notaf+=nota
    prom=cal_prom(notaf,cantnotas)
    print("el promedio del alumno ", a ," es ", prom)
    if prom>=40:
        print(f"el alumno {a} aprobo")
    else:
        print(f"el alumno {a} reprobo")
    promcurso+=prom
promcurso/=cantalumnos
print(f"el promedio del curso fue de {promcurso}")


def name(n):
    print(f"I nombre es {n}")
    
        
# name("Link")

def calcula_iva(i):
   return i*0.19

total=100

iva_calculado=calcula_iva(total)

print(f" El iva es {iva_calculado} , tl total con iva es {iva_calculado+total}")


