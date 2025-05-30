# Nivel Básico
#Suma de dos números
#Escribe una función suma(a, b) que retorne la suma de dos números.

def suma(a,b):
    return a+b


while(True):
    try:
      numero1 = int(input("ingresar numero a capturar"))
      numero2 = int(input("ingresar numero a capturar"))
      break
    except ValueError:
        print("deben ser variables numerales")

print(suma(numero1,numero2))



#Número par o impar
#Crea una función es_par(numero) que devuelva True si el número es par y False si es impar.

variable = int(input("ingresar numero"))
def par(numero):
 if numero % 2 == 0:
     return  True
 else:
     return  False

print(par(variable))

#Mayor de tres números
#Escribe una función mayor_de_tres(a, b, c) que devuelva el mayor de tres números dados.

"""
def mayordetres (number1,number2,number3):
    if number1 > number2 and number1 > number3:
        return "digito uno es mayor al segundo digito y el tercer digito"
    elif number2 > number1 and number2 > number3:
        return "digito dos es mayor al primer digito y el tercer digito"
    elif number3 > number1 and number3 > number2:
        return "digito tres es mayor al segundo y tecer digito"
    else:
        return "error"
    
def mayoria(a,b,c):
    f = max(a,b,c)
    return f

print(mayordetres(1,2,3))
print(mayoria(1,2,3))
"""
#Contar vocales en una cadena
#Define una función contar_vocales(cadena) que cuente cuántas vocales hay en una cadena.

"""

def contarvocales (cadena):
    contador = 0 
    vocales = "AEIOUaeiou"

    for caracteres in cadena:
        if caracteres in vocales:
            contador += 1
    return contador 


while True:
    cadena_a = input("Ingrese una cadena (o escriba 'salir' para terminar): ")
    if cadena_a.lower() == "salir":
        break
    cantidad_vocales = contarvocales(cadena_a)
    print(f"Número de vocales: {cantidad_vocales}")

"""

#Inverso de una cadena
#Escribe una función invertir_cadena(cadena) que devuelva la cadena invertida.

"""
def invertir_cadena():
    frase = input("Introduce una frase: ")
    return (frase[::-1])

print(invertir_cadena())
"""


#Nivel Intermedio
#Factorial de un número
#Crea una función factorial(n) que devuelva el factorial de un número utilizando recursión.
def factorial(n):
    if n <= 1:
        return  1
    else:
        return  n * factorial(n - 1)
print(factorial(2))
#Comprobar si una palabra es palíndromo
#Define una función es_palindromo(palabra) que determine si una palabra es igual al revés.
def comprobar (palabra):
    a = palabra[::-1]
    if palabra == a:
        return "palabra palindroma"
    else:
       return "la palabra no es palindroma"

print(comprobar("ala"))

#Generador de números primos
#Crea una función primos_hasta(n) que devuelva una lista con todos los números primos hasta n.

#Conversor de grados
#Escribe una función convertir_temperatura(valor, unidad) que convierta entre Celsius y Fahrenheit.

#Contador de palabras únicas
#Crea una función contar_palabras_unicas(texto) que reciba una cadena y retorne cuántas palabras únicas hay.
