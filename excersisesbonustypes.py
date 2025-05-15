
# int: entero
numero_entero = 10

# float: número decimal
numero_decimal = 3.14

# str: cadena de texto
texto = "Hola mundo"

# bool: booleano
valor_verdadero = True
valor_falso = False

# list: lista
mi_lista = [1, 2, 3]

# tuple: tupla
mi_tupla = (1, 2, 3)

# set: conjunto
mi_conjunto = {1, 2, 3}

# dict: diccionario
mi_diccionario = {'a': 1, 'b': 2}

# NoneType: valor nulo
nulo = None


# --- Casting: Conversión de tipos ---

# str a int
numero_desde_texto = int("42")  # 42

# str a float
decimal_desde_texto = float("3.14")  # 3.14

# int a str
texto_desde_entero = str(123)  # "123"

# float a int (trunca los decimales)
entero_desde_decimal = int(3.99)  # 3

# int a float
decimal_desde_entero = float(5)  # 5.0

# str a bool
booleano_desde_texto = bool("hola")  # True

# bool a int
uno = int(True)   # 1
cero = int(False) # 0


# --- Conversión de letras a números y viceversa (ASCII) ---

# De letra a número
codigo_A = ord("A")  # 65
codigo_a = ord("a")  # 97

# De número a letra
letra_65 = chr(65)   # "A"
letra_97 = chr(97)   # "a"

# Ejemplo con input
# letra = input("Ingresa una letra: ")
# print(f"El código ASCII de {letra} es {ord(letra)}")
