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

#Contar vocales en una cadena
#Define una función contar_vocales(cadena) que cuente cuántas vocales hay en una cadena.

#Inverso de una cadena
#Escribe una función invertir_cadena(cadena) que devuelva la cadena invertida.




#Nivel Intermedio
#Factorial de un número
#Crea una función factorial(n) que devuelva el factorial de un número utilizando recursión.

#Comprobar si una palabra es palíndromo
#Define una función es_palindromo(palabra) que determine si una palabra es igual al revés.

#Generador de números primos
#Crea una función primos_hasta(n) que devuelva una lista con todos los números primos hasta n.

#Conversor de grados
#Escribe una función convertir_temperatura(valor, unidad) que convierta entre Celsius y Fahrenheit.

#Contador de palabras únicas
#Crea una función contar_palabras_unicas(texto) que reciba una cadena y retorne cuántas palabras únicas hay.
