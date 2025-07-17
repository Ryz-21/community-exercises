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


#lista = [1,2,3,4,5,6,7,8,9,10]

#lista_invertida = lista[::-1]

#print(",".join(map(str,lista_invertida)))


#Ejercicio 6
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
#pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar
#por pantalla las asignaturas que el usuario tiene que repetir.


"""
cursos = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

while True:
    asignatura = input("Ingresar asignatura (o escribe 'salir' para terminar): ")
    if asignatura.lower() == "salir":
        break

    if asignatura in cursos:
        nota = float(input(f"Ingresar nota que sacaste en {asignatura}: "))
        if nota >= 10:
            print("Está aprobado. Se eliminará del curso.")
            cursos.remove(asignatura)
        else:
            print("No aprobado. Deberás repetirla.")
    else:
        print("Esa asignatura no está en la lista del curso.")

# Mostrar asignaturas pendientes
print("\nAsignaturas que debes repetir:")
for materia in cursos:
    print(materia)

"""
#Ejercicio de 7 
#Escribir un programa que almacene el abecedario en una lista,
# elimine de la lista las letras que ocupen posiciones múltiplos de 3,
# y muestre por pantalla la lista resultante.

"""

#creamos el abacedario como la lista inicial 
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
              "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", 
              "t", "u", "v", "w", "x", "y", "z"]
#creamos la nueva lista la que almacenara el resultado

nueva_lista = [letra_buscar for i ,  letra_buscar in enumerate(abecedario) if (i + 1)%3 !=0]
#utilizo ennumerate por que me permite retornar el indice y el valor.
#i + 1 indica que comenzaremos desde el indice 1 y el modulo % 3devuelvo el resto de dividir (i+1) % 3
#que sea diferente de cero 
print(f"la lista de abecarios inicial es {abecedario}")
print(f"la nueva ista es {nueva_lista}")

"""

#ejrcicio numero 8
#Escribir un programa que pida al usuario una palabra y
# puestre por pantalla si es un palíndromo.
"""

def palindromo():
    palabra = input("ingresar la palabra")
    a = palabra[::-1]
    if a == palabra:
        print("la palabra es palindroma")
    else:
        print("error")

print(palindromo())
"""

#Ejercicio 9
#Escribir un programa que pida al usuario una palabra
#y muestre por pantalla el número de veces que contiene
#cada vocal.

"""""
lista_vocales = ["a","e","i","o","u"]

def busquedavocales(palabra):
    palabra = palabra.lower()
    for vocal in lista_vocales:
        cantidad = palabra.count(vocal)
        print(f"la vocal es {vocal} la cantidad de veces que aparece es {cantidad}")

print(busquedavocales("pepito"))
"""

#Ejercicio 10
#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
#y muestre por pantalla el menor y el mayor de los precios.

lista_precios = [50,75,46,22,80,65,8]
precio_maximo = max(lista_precios)
precio_minimo = min(lista_precios)

print(f"el precio mayor es {precio_maximo} y el precio menor es {precio_minimo}")
