#Ejercicio 1
#Escribir un programa que pregunte al usuario su edad y muestre
#por pantalla si es mayor de edad o no.


"""
years = int(input("insert your years of life xd"))

if years < 18:
    print("you cannot be under 18")
else:
    print("you are over 18")
"""

#Ejercicio 2
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
#por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

"""
password = "pepito12345"

password1 = input("insert password")

if password.lower() == password1.lower():
    print("successful")
else:
    print("error")

"""
#Ejercicio 3
#Escribir un programa que pida al usuario dos números
# y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

"""
number1 = int(input("insertar primer numero"))
number2 = int(input("insertar segundo numero"))
if  number2 == 0:
    print("error")
else:
    resultado = number1 / number2
    print(resultado)

"""

#Ejercicio 4
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

"""
number = int(input("ingresar numero para verificar"))
if number % 2 != 0:
    print("numero impar")
else:
    print("numero par")
"""

#Ejercicio 5
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales
#o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos
#mensuales y muestre por pantalla si el usuario tiene que tributar o no.

"""
edad = int(input("ingresar edad del usuario"))
dinero = float(input("ingresar sueldo del usuario"))

if edad < 16 or dinero < 1000:
    print("error no puede tributar")
else:
    print("puede tributar")
"""

#Ejercicio 6
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
#El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres
#con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario
#su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

"""
nombre = input("ingresar nombre para determinar su grupo").strip().capitalize()
genero = input("ingresar genero en formato M = Masculino o F = Femenino").strip().upper()

if nombre < "M" and genero == "F":
    print("pertenece al grupo A")
elif nombre > "N" and genero == "M":
    print("pertenece al grupo A")
else:
    print("Pertenece al grupo b")
"""

#Ejercicio 7
#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo
#que le corresponde.
#Renta	Tipo impositivo
#Menos de 10000€	5%
#Entre 10000€ y 20000€	15%
#Entre 20000€ y 35000€	20%
#Entre 35000€ y 60000€	30%
#Más de 60000€	45%

"""
renta = float(input("ingresar renta anual"))

if renta < 10000:
    print("el tipo impositivo es de el 5%")
elif 10000 <= renta < 20000:
    print("el tipo impositivo es de el 15%")
elif 20000 <= renta <35000:
    print("el tipo impositivo es de el 20%")
elif 35000 <= renta <60000:
    print("el tipo impositivo es de el 30%")
elif renta > 60000:
    print("el tipo impostivo es del 40%")
"""

#Ejercicio 8
#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden
# obtener en la #evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios.
# Los puntos que pueden conseguir #los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios
# entre las cifras mencionadas. A continuación se #muestra una tabla con los niveles correspondientes a cada puntuación.
# La cantidad de dinero conseguida en cada nivel es de #2.400€ multiplicada por la puntuación del nivel.

#Nivel	Puntuación
#Inaceptable	0.0
#Aceptable	0.4
#Meritorio	0.6 o más
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento,
# así como la cantidad de dinero #que recibirá el usuario.


puntaje = float(input("ingresar os puntos que deben obtener"))

dinero = 2400

if puntaje == 0.0:
    print("su sueldo es", dinero)
elif puntaje == 0.4:
    print("su sueldo es" , dinero*0.4)
elif puntaje >= 0.6:
     print("su sueldo es" , dinero*0.6)
else:
    print("error esta fuera de rango")



#Ejercicio 9
#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática
# #el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el
# #precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si #es mayor de 18 años, 10€.

edad = int(input("ingresar tu edad para los juegos"))

if edad < 4:
    print("puede ingresar gratis")
elif 4 <= edad <= 18:
    print("debes pagar 5 euros")
else:
    print("paga 10 euros")

#Ejercicio 10
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no
# , y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print("Bienvenido a la pizzería Bella Napoli")
print("¿Desea una pizza vegetariana?")
respuesta = input("Responda 'sí' o 'no': ").lower()

if respuesta == "sí" or respuesta == "si":
    print("Ha elegido una pizza vegetariana.")
    print("Ingredientes disponibles:")
    print("1. Pimiento")
    print("2. Tofu")
    opcion = input("Elija el número del ingrediente (1 o 2): ")

    if opcion == "1":
        ingrediente = "Pimiento"
        print("Pizza vegetariana con mozzarella, tomate y", ingrediente)
    elif opcion == "2":
        ingrediente = "Tofu"
        print("Pizza vegetariana con mozzarella, tomate y", ingrediente)
    else:
        print("Opción no válida.")

elif respuesta == "no":
    print("Ha elegido una pizza no vegetariana.")
    print("Ingredientes disponibles:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    opcion = input("Elija el número del ingrediente (1, 2 o 3): ")

    if opcion == "1":
        ingrediente = "Peperoni"
        print("Pizza no vegetariana con mozzarella, tomate y", ingrediente)
    elif opcion == "2":
        ingrediente = "Jamón"
        print("Pizza no vegetariana con mozzarella, tomate y", ingrediente)
    elif opcion == "3":
        ingrediente = "Salmón"
        print("Pizza no vegetariana con mozzarella, tomate y", ingrediente)
    else:
        print("Opción no válida.")

else:
    print("Respuesta no válida. Por favor escriba 'sí' o 'no'.")
