# text
textData = "Hello world"

# numeric
integerNumber = 1
floatNumber   = 1.5
complexNumber = 1j

# sequence
listType  = [1,2,3,'hello']
tupleType = (1,2,3)
rangeType = range(6)

# mapping
dictionaryType = {"name": "Peter", "age": 24}

# set types
setType       = {"apple", "banana", "cherry"}
frozenSetType = frozenset({"apple", "banana", "cherry"})

# booleans 
booleanVar = True
booleanVar = False

# binary
bytesVar      = b"Hello"
byteArray     = bytearray(5)
memoryViewVar = memoryview(bytes(5))

#################################################################
#################################################################
################### OPERACIONES CON LAS LISTAS ##################
#################################################################
#################################################################

# Las listas pueden almacenar cualquier tipo de dato

def listFunction():
    miLista = ['Manolo', 'Pepe', 'Maria', 150]
    print(miLista[:])   # impresión por pantalla de la lista completa
    print(miLista)      # impresión por pantalla de la lista completa
    print(miLista[1])   # impresión del índice 1 de la lista
    print(miLista[-2])  # python admite indices negativos. Da la vuelta al list partiendo como referencia de la pos = 0
    print(miLista[0:2]) # imprime un rango de indices. El primer valor del rango es inclusivo, el segundo es EXCLUSIVO
    print(miLista[1:3]) # imprime un rango de indices. El primer valor del rango es inclusivo, el segundo es EXCLUSIVO
    print(miLista[:2])  # python sobreentiende que si no se especifica, el valor de inicio del rango será 0
    print(miLista[1:])  # python sobreentiende que si no se especifica el valor final, tirará hasta el final de la lista
    print(miLista.index('Pepe')) # imprime la posición del elemento 'Pepe'. Si el elemento está duplicado, devolverá el primero que encuentre
    print('Pepe' in miLista) # devuelve True o False si el elemento 'Pepe' existe en la lista.

    miLista.append('itemAñadidoAppend') # agrega elementos al final de la lista
    print(miLista)

    miLista.insert(1, 'itemAñadidoInsert') # agrega elementos en la posición indicada
    print(miLista)

    miLista.extend(['elementoDeLaNuevaLista1', 'elementoDeLaNuevaLista2']) # agrega un conjunto de elementos a la lista. Se le pasa por parámetro otra lista (o un Iterable)
    print(miLista)

    miLista.remove("Pepe") # elimina el elemento que le pase por parámetro
    print(miLista)

    miLista.pop() # elimina el ultimo elemento de la lista
    print(miLista)

    # el operador + actúa como concatenador de listas
    print([1,2,3] + [4,5,6])

    # el operador * actúa como repetidor
    print([1,2,3] * 3)

#################################################################
#################################################################
##################### OPERACIONES CON TUPLAS ####################
#################################################################
#################################################################

# Las tuplas son listas inmutables
# No se pueden modificar despues de crearlas
# No permiten añadir, eliminar, mover elementos
# No permiten búsquedas (index())
# Permite extraer porciones, pero el resultado de la extracción es una tupla nueva
# Permiten comprobar si un elemento existe dentro de la tupla

# Son más rápidas en runtime
# Ocupan menos espacio en memoria
# Mayor rendimiento
# Se pueden utilizar como clave en un dictionary

def tupleFunction():
    miTupla = ('elemento 1', 'elemento 2', 'elemento 3') # los paréntesis son opcionales
    print(miTupla[1]) # acceso al índice 1 de la tupla



# EJECUCIÓN DE LOS EJEMPLOS
# listFunction()
tupleFunction()