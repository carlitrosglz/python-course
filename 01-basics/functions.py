# SINTAXIS PARA DECLARACIÓN DE FUNCTIONS

def funcionSinParametros():
    # código de la función...
    variable1 = "hola"
    return variable1

def funcionConParametros(arg1, arg2):
    variable1 = "adios"
    return variable1 + arg1 + arg2

print(funcionSinParametros())
print(funcionConParametros(' manolo', 'kabezabolo'))