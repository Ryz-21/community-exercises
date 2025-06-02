#Ejercicio 1
#
#Escribir un programa que almacene las asignaturas de un curso
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.


lista = []

while(True):
    try:
        cursos = input("ingresar que curso sigue")
        if cursos == "exit":
            break
        else:
            lista.append(cursos)
            print(lista)
    except:
        print("error algo salio mal en la agregacion")
    finally:
        print("finaizacion del programa")




#Ejercicio 2
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
#Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
#onde <asignatura> es cada una de las asignaturas de la lista.

asginaturas = ["Matemáticas","Física", "Química", "Historia" , "Lengua"]

nombre = input("ingresar nombre")

print(f"{nombre} yo estudio cada una de las asignaturas de este año que son {asginaturas}")
