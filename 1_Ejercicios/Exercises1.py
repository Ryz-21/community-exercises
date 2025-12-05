#Ejercicios de Tipos de Datos Simples
#Ejercicio 1
#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

"""
print("hola mundo")
"""

#Ejercicio 2
#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

"""
variable = "hola mundo"
print(variable)
"""

#Ejercicio 3
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

"""
nombre = input("ingresar nombre")
print(f"hola mundo {nombre}")
"""

#Ejercicio 4
#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética (3+2/2.5)^2

"""
operacion = (3+2/2.5)**2
print(operacion)
"""

#Ejercicio 5
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

"""
number = int(input("ingresar el numero de horas trabajadas"))
cost = float(input("ingresar el precio por hora"))

pago = number*cost

print(pago)
"""



#Ejercicio 6
#Escribir un programa que lea un entero positivo,
# introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta . La suma de los
#primeros enteros positivos puede ser calculada de la siguiente forma: m = n(n+1)/2


"""
number = int(input("ingresar numero positivo"))

if number < 0:
    print("error debe ser mayor a 0")
else:
    n = number*(number+1)/2
    print(n)
"""


#Ejercicio 7
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable,
#  y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

"""
peso = float(input("ingresar peso porfavor"))
estatura = float(input("ingresar estatura"))

imc = peso / estatura**2

print(f"el imc es {imc} índice de masa corporal calculado")
"""



#Ejercicio 8
#Escribir un programa que pida al usuario dos números enteros
#  y muestre por pantalla la <n> entre <m> da un cociente <c>
#  y un resto <r> donde <n> y <m> son los números introducidos por el usuario, 
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.


"""
n = int(input("ingresar numero entero"))
m = int(input("ingresar numero entero"))

c = n//m # cociente
r = n & m #resto

print(f"<c> {c}")
print(f"{r} <r>")

"""




#Ejercicio 9
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
#  y muestre por pantalla el capital obtenido en la inversión.

"""
"""
#Total = Dinero × (1 + Interés anual) elevado al tiempo
#tiempo*dinero*interes anual
"""
number = float(input("ingresar una cantidad de dinero a invertir"))
interes = float(input("ingresar interes anual"))
tiempo = int(input("ingresar años a tener la inversion"))

if number < 0 or interes < 0 or tiempo < 0:
    print("error no pueden ser menor a 0")
else:
            total = number*(1+interes/100) ** tiempo
            print(f"el dinero total obtenido es {total}")
"""


#Ejercicio 10
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y
#  la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y 
# muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa 
# que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

"""
payaso = 112
muñeca = 75

cantidad1 = int(input("ingresar cantidad de payasos"))
cantidad2 = int(input("ingresar cantidad de muñecas"))

peso1= cantidad1*payaso
peso2= cantidad2*muñeca
total = peso1+peso2

print(f"el total de peso es {total} gr" )
"""


#Ejercicio 11
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, 
# que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
#  Escribir un programa que comience leyendo la cantidad de dinerode positada en la cuenta de ahorros, introducida por el usuario.
#  Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.

"""
interes = 0.04
#no se aumentan hasta finales de año 

dinner = float(input("ingresar cantidad de dinero"))

for i in range (1,3+1):
    dinner *= (1+interes)
    print(f"el {i} año el dinero total fue {dinner}")
"""



#Ejercicio 12
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que 
# comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan
# , el descuento que se le hace por no ser fresca y el coste final total.
#Descuento = Precio original * (Porcentaje de descuento / 100

"""
precio = 3.49

barranodia = int(input("ingresar cantidad de barra que no son del dia"))

descuento = precio*(60/100)
nuevoprecio = precio-descuento
preciototal = nuevoprecio*barranodia
print("precio habitual de la barra es" , precio)
print("el descuento que tiene hoy seria" , descuento)
print("el total de su pedido seria",preciototal)
"""

