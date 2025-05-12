#1 Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""

palabra = input("escribir una palabra para mostrar  ")

for i in range (10):
    print(palabra)
"""

"""
cont = 0
palabra = input("escribir una palabra para mostrar  ")

while cont < 10:
    print(palabra)
    cont+=1
"""
    
# 2 Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
# todos los años que ha cumplido (desde 1 hasta su edad).


"""
edad = int(input("escribir edad que tienes"))

cont = 1

while cont<=edad:
     if cont < 5:
      print(f"{cont} año correspondiente")
     else:
        print(f"{cont} años correspondientes")
     cont+=1
"""


#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo y
#muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


"""
number = int(input("Escribe un número para mostrar los impares desde 1: "))
#"%" devuelve el resto de una division
#x % 2 == 0 numero par 
#x % 2 != 0 numero impar
#(number,-1,-1): decendente
#(1,number+1): acedente 

lista = []
if number > 0:
    print("su numero es aprobado")
    for i in range (1,number+1):
        if i % 2 != 0: 
            lista.append(i)
            print(lista)
else:
    print("error")
"""


#4 Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
#  la cuenta atrás desde ese número hasta cero separados por comas.

"""
lista  = []
numero = int(input("ingresar numero entero positivo"))
if numero > 0:
    print("su numero es aprobado")
    
    for i in range (numero,-1,-1):
        lista.append(i)
    print(lista)
else:
    print("porfavor ingresar numero entero")
"""

#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

"""
dinner = float(input("ingresar cantidad de dinero a invertir"))
interes_anual = float(input("Ingresa el interés anual en porcentaje (por ejemplo, 5 para 5%): "))
time = int(input("ingresar cantidad de años a ahorrar"))

if dinner < 100:
     print("error no puede ser menor a 100")
elif time < 1:
        print("no puede ser menor que uno")
else:
     for i in range(1,time+1):
            dinner *= (1,interes_anual/100) 
            print(f"El dinero al final del año {i} es: {dinner:.2f}")
"""


#Ejercicio 6
#Escribir un programa que pida al usuario un número entero y muestre por pantalla
#un triángulo rectángulo como el de más abajo, de altura el número introducido.


"""
number = int(input("escribir un numero de el tamaño del triangulo"))

for i in range (number):
    print("*"*i)
"""



#Ejercicio 7
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
number = int(input("escribir un numero"))

for i in range (1,10+1):
    print(f"el resultado del {number} multiplicado por {i} es ",i*number)
"""



#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo como el de más abajo.

number = int(input("Ingrese un número para formar el triángulo rectángulo: "))

current_odd = 1  

for i in range(1, number + 1):
    fila = []
    for j in range(i):
        fila.append(current_odd)
        current_odd += 2  
    fila.reverse() 
    print(" ".join(str(num) for num in fila))


#9 Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

"""
password = "Pepito2145"

interPass = input("insert into password")


while  interPass != password:
 interPass = input("try insert into password")

if interPass == password:
    print("susefull")
"""

# 10 Escribir un programa que pida al usuario un número entero y 
#muestre por pantalla si es un número primo o no.
"""
number = int(input("escribir numero"))

if number < 2:
    print("error no es un numero primo")
else:
    primo = True #DAMOS POR HECHO
    for i in range (2,number):
        if number % i == 0:
            primo = False
            break

if primo == True:
    print("si es primo")
else:
    print("no es primo")
"""


#Ejercicio 11
#escribir un programa que pida al usuario una palabra y luego muestre por pantalla u
#na a una las letras de la palabra introducida empezando por la última.

"""
palabra = input("escribir palabra a pasar a letras")

for i in range (len(palabra)-1,-1,-1):
    print(palabra[i])
"""

#12 Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
#y muestre por pantalla el número de veces que aparece la letra en la frase.


"""
frase = input("escribir frase")
palabra = input("escribir letra a buscar en la frase")


a = frase.count(palabra)

print(a)
"""

#13 Escribir un programa que muestre el eco de todo lo que el usuario introduzca 
#hasta que el usuario escriba “salir” que terminará.

"""
eco = input("escribir palabra para formar el eco")

while eco != "salir":
    print(eco)
    eco = input("escribir palabra para formar el eco")
    
print("salida exitosa")
"""


"""
def bussquedalinealmultiple (lista,valor):

    indice = [i for i ,in enumerate(lista) if valor == i]
    return indice if indice else -1
"""

"""
def busquedalineal (lista, valor):
    for i in enumerate(lista):
        if i == valor:
            return i
    return -1
"""

"""
def busquedamatriz (matriz,valor):
    for i in enumerate(matriz):
        for e in enumerate(i):
            if e == valor:
                return i , e
    return -1 
"""


"""
def busquedamatrizmultiple (matriz,valor):
    indice = [(i,e) for i ,fila in enumerate(matriz)
               for e , element in enumerate(fila) if element == valor]
    return indice if indice else -1
"""
