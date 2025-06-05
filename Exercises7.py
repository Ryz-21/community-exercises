#Ejercicio 1
#
#Escribir un programa que almacene las asignaturas de un curso
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

"""
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

"""


#Ejercicio 2
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
#Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
#onde <asignatura> es cada una de las asignaturas de la lista.
"""
asginaturas = ["Matemáticas","Física", "Química", "Historia" , "Lengua"]

nombre = input("ingresar nombre")

print(f"{nombre} yo estudio cada una de las asignaturas de este año que son {asginaturas}")
"""



#Ejercicio 3
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
#es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

"""
lista1 = []
notas = []

while(True):
    try:
        cursos = input("ingresar que curso sigue")
        lista1.append(cursos)
        nota = float(input("ingresar nota del curso"))
        notas.append(nota)     
        seguir = input("deseas seguir?")
        if seguir == "no":
             print(f"los cursos son {lista1} y las notas son {notas}")
             break
    except:
        print("error algo salio mal en la agregacion")
    finally:
        print("finaizacion del programa")
"""


#Ejercicio 4
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

"""
lista = []

while(True):
    try:
        numeros = int(input("ingresar los numeros de la loteria"))
        lista.append(numeros)
        lista.sort()
        seguir = input("deseas seguir?")
        if seguir == "no":
            print(f"la lista ordenada es{lista}")
            break
    except:
        print("error en la lista comprobar agregacion")
"""
        
#Ejercicio 5
#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

lista = [1,2,3,4,5,6,7,8,9,10]

print(', '.join(str(num) for num in lista[::-1]))

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista
#pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
#Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
