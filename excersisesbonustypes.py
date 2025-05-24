
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

# Entero (int)
x = 10
print(type(x), x)  # <class 'int'> 10

# Flotante (float)
y = 3.14
print(type(y), y)  # <class 'float'> 3.14

# Cadena de texto (str)
s = "Hola"
print(type(s), s)  # <class 'str'> Hola

# Booleano (bool)
b = True
print(type(b), b)  # <class 'bool'> True

# Lista (list) - Mutable
l = [1, 2, 3]
print(type(l), l)  # <class 'list'> [1, 2, 3]

# Tupla (tuple) - Inmutable
t = (1, 2, 3)
print(type(t), t)  # <class 'tuple'> (1, 2, 3)

# Diccionario (dict) - Clave-valor
d = {"a": 1, "b": 2}
print(type(d), d)  # <class 'dict'> {'a': 1, 'b': 2}

# Conjunto (set) - Sin duplicados
s = {1, 2, 3, 3, 2, 1}
print(type(s), s)  # <class 'set'> {1, 2, 3}

