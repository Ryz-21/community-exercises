import math

#TRY ! EXCEPT ! FINALLY

#tipos de errores

#ValueError: Conversión de tipos inválida.

#ZeroDivisionError: División entre cero.

#FileNotFoundError: Archivos que no existen.

#IndexError: Índices fuera de rango en listas.

#KeyError: Acceso a claves inexistentes en diccionarios.

#TypeError: Operaciones con tipos incompatibles.

#IOError / OSError: Problemas de entrada/salida (archivos, red).

#ImportError: Problemas al importar módulos.

#AttributeError: Acceso a atributos inexistentes.

#Exception (genérica): Para capturar errores no previstos

#Programa que se encargue de sumar dos numeros : con try

"""
try: #intenta
    number1 = int(input("ingresar numero"))
    number2 = int(input("ingresar numero dos"))
    result = number1 * number2
except: #si no puede
    print("debes introducir numeros no letras")
finally: # si o si se imprime
    print("esto siempre se va a ejecutar")

"""


#control de las exceptiones con while

"""
while(True):
    try:
      number1 = int(input("ingresar numero"))
      number2 = int(input("ingresar numero dos"))
      result = number1 * number2
      print(result)
      break
    except:
       print("ingresar numero no letras")
    finally:
       print("siempre")
"""


#Pide al usuario dos números e imprime el resultado de la división. Captura el error si el segundo número es cero.

"""
while(True):
    try:
        number1 = int(input("ingresar primero numero"))
        number2 = int(input("ingresar segundo numero"))
        a = number1 / number2
        print(a)
        break
    except ZeroDivisionError:
        print("numero devidido por 0 no se puede")
    finally:
        print("siempre se ejecuta")
"""

#Solicita una edad al usuario. Si escribe algo que no es número entero, muestra un mensaje de error.

"""
while (True):
   try:
     edad = int(input("ingresar valor"))
     print("su edad esta correcta")
   except ValueError:
      print("su valor debe ser entero no otro")
   finally:
      print("siempre se ejecuta")
"""


#Abre un archivo de texto que no existe y maneja la excepción correspondiente para mostrar un mensaje al usuario.
"""
while (True):
    try:
        archivo =   open("hola.txt" , "r")
        contenido = archivo.read()
        print(contenido)
    except FileExistsError:
        print("el archivo no existe. Verifica la ruta o el nombre")
    finally:
        print("error")
"""


#Crea una lista con 3 elementos y pide un índice al usuario para acceder a un elemento. Maneja el error si el índice es inválido.



"""
lista = [1,2,3]
while(True):
  try:
      indice = int(input("ingresar valor que quieres recuperar"))
      print("elemento en ese indice es" , lista[indice])
      break     
  except IndexError:
     print("indice fuera de rango")
  except ValueError:
     print("error debe ingresarse un numero entero")
  finally:
     print("siempre se ejecuta")
"""



#Solicita al usuario una cadena y convierte el primer carácter a entero. Maneja el error si no es un dígito.

"""
while(True):
    try:
        cadena = input("ingresar una cadena a convertir")
        valor = cadena[0]
        print(valor)
        convertir = ord(valor)
        print(convertir)
        break
    except ValueError:
        print("ingresar una cadena valida para ingresar")
    finally:
        print("siempre se ejecuta")
"""

#Intenta abrir un archivo, leer su contenido y siempre ciérralo en el bloque finally, aunque ocurra un error.


"""
file = "notas.txt"

while True:
    try:
        f = open(file, "r", encoding="utf-8")
        contenido = f.read()
        print(contenido)
        break  # Si la lectura es exitosa, salimos del bucle
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        break  # Si no existe, también salimos
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break
    finally:
        try:
            f.close()
        except:
            pass  

"""

#Simula un sistema de autenticación que lanza una excepción si el usuario o contraseña están vacíos. Usa try-except-finally.

"""
admin = "leo"
password ="samael102104"
while(True):
    try:
        usuario = input("ingresar usuario")
        contraseña = input("ingresar contraseña")
        if usuario == "" or  contraseña == "":
            raise ValueError("usuario o contraseña no pueden estar vacios")
        else:
         if usuario == admin and password == contraseña:
            print("autenticacion correcta")
            break
         else:
             print("usuario o contraseña incorrecto")

    except ValueError as ve:
        print(f"error{ve}")
    finally:
        print("conexion correcta")
"""

#Realiza una operación matemática (raíz cuadrada) y lanza una excepción si el número ingresado es negativo.
"""
while(True):
    try:
        numero = int(input("ingresar numero a sacar raiz cuadrada"))

        if numero < 1 :
            raise ValueError("el numero no puede ser menor a 1")
        else:
            raiz = math.sqrt(numero)
            print("la raiz cuadrada es:" , raiz)
    except ValueError as ve:
     print(f"error{ve}")
    finally:
        print("conexion establecida")
"""
#Simula la compra de un producto. Si el usuario ingresa un valor no numérico para la cantidad o el precio
# captura el error.

"""
opciones = {"zapatos": 120, "casaca":80 , "polo":30}

opcion = input("ingresar producto a querer comprar zapatos , casaca , polo")
try:
  if opcion in opciones:
     print("producto encontrado")

     cantidad = int(input("ingresar cantidad de producto que deseaa llevar"))
     if cantidad < 1:
         raise ValueError("no puede ser menor a 1")
     else:
         print("confirmado")

     precio = opciones[opcion]

     total = cantidad*precio
     print("el precio a pagar es", total)
     pago = float(input("ingresar con cuanto va a cancelar el pedido"))
     if pago < total:
         raise  ValueError(f"no puede ser menor a {total} ")
     print("confirmado")
  else:
     print("producto no encontrado")
except ValueError as e:
 print(f"error: {e}")
finally:
    print("ejecucion finalizada")
"""

#Escribe una función que recibe dos parámetros numéricos.
# Si alguno no es número, lanza y captura una excepción.

"""
def suma (a,b):
 try:
     resultado = a+b
     return resultado
 except TypeError:
     print("no son numeros no se puede sumar")

print(suma(23,4))
"""
