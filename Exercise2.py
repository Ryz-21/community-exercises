#Ejercicios de Cadenas
#Ejercicio 1
#Escribir un programa que pregunte el nombre del usuario en la consola
#y un número entero e imprima por pantalla en líneas distintas el nombre del
#usuario tantas veces como el número introducido.

"""
name = input("ingresar nombre del usuario")
number = int(input("ingresar un numero entero"))

for i in range (number):
    print(f"el nombre utilizado es {name}")

print((name + "\n")*number)
"""

#Ejercicio 2
#Escribir un programa que pregunte el nombre completo del usuario en la consola y después
#muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras
#minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre
#y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas
#y minúsculas como quiera.

"""
name = input("insertar nombre completo")
#1
for i in range (3):
    if i == 0:
        print(name.lower())
    elif i == 1:
        print(name.upper())
    elif i == 2:
        print(name.title())
"""

#2
"""
name = input("insertar nombre completo")
print(name.lower())
print(name.upper())
print(name.title())
"""

#Ejercicio 3
#Escribir un programa que pregunte el nombre del usuario en la consola
# y después de que el usuario lo introduzca muestre por pantalla <NOMBRE>
# tiene <n> letras, donde <NOMBRE> es el nombre de usuario
#en mayúsculas y <n> es el número de letras que tienen el nombre.

#count() cantidad de veces
#len() cuenta la cantidad total

"""
name = input("ingresar nombre del usuario")
print(f"el nombre es {name.upper()} y tiene la cantidad de letras {len(name)}" )
"""


#Ejercicio 4
#Los teléfonos de una empresa tienen el siguiente formato
# prefijo-número-extension donde el prefijo es el código del país +34,
# y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
# Escribir un programa que pregunte por un número de teléfono con este formato
# y muestre por pantalla el número de teléfono sin el prefijo y la extensión. []
#split tambien
"""
number = input("ingresar numero de telefono con formato {+34-913724710-56}")
telefonosolo = number[4:13]
print(telefonosolo)

"""

#Ejercicio 5
#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por
#pantalla la frase invertida frase[inicio:fin:paso]


"""
#1
frase = input("Introduce una frase: ")
print(frase[::-1])
"""


"""
#2
frase = input("ingresar la frase corespondiente al pedido")
fraseA = ""

for i in range (len(frase)-1,-1,-1):
    fraseA += frase[i]

print(fraseA)
"""

#Ejercicio 6
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
#y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

"""
1#
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))
"""

"""
#2
frase = input("ingresar frase")
vocal = input("ingresar vocal")

vocal = vocal.lower()
frase_ = ""

for letra in frase:
    if letra == vocal:
        frase_ += letra.upper()
    else:
        frase_ += letra

print("Frase modificada:", frase_)
"""


#Ejercicio 7
#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre
# por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @)
# pero con dominio ceu.es.

"""
correo = input("ingresar correo electronico")
print(correo.replace("@gmail.com","@ceu.es"))

"""

#Ejercicio 8
#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
# y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

"""
precio = input("ingresar precio con decimales")

euros,centimos= precio.split(".")

print(euros)
print(centimos)


"""

#Ejercicio 9
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
# dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
# Adaptar el programa anterior para que también funcione cuando
# el día o el mes se introduzcan con un solo carácter.


"""
from datetime import datetime

fecha_nac = input("ingresar fecha de nacimiento en formato dd/mm/aa ")
fecha = datetime.strptime(fecha_nac,"%d/%m/%y")
print("dia:",fecha.day)
print("mes:",fecha.month)
print("año:",fecha.year)

"""

#Ejercicio 10
#Escribir un programa que pregunte por consola por los productos de una cesta de la compra
# , separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

"""
Carrito = input("ingresar productos de una cesta de compra separado por comas")
productos = Carrito.split(",")
for producto in productos:
        print(producto.strip())
"""
"""
Carrito = input("ingresar productos de una cesta de compra separado por comas")
print(Carrito.replace("," , "\n"))
"""


#Ejercicio 11
#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades
# y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario
# con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total
# con 8 dígitos enteros y 2 decimales.

"""
nombre = input("Ingresar nombre del producto: ")
precio = float(input("Ingresar precio del producto: "))
unidades = int(input("Ingresar número de unidades: "))
total = precio * unidades
print(f"Producto: {nombre}")
print(f"Precio unitario: {precio:09.2f}")  # 6 dígitos enteros + '.' + 2 decimales = 9 total
print(f"Unidades: {unidades:03d}")
print(f"Costo total: {total:010.2f}")      # 8 enteros + '.' + 2 decimales = 10 total
"""
