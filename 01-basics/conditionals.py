#################################################################
#################################################################
############################ IF ELSE ############################
#################################################################
#################################################################

# SINTAXIS BÁSICA:
    # if
    # elif
    # else

# Es posible concatenar operadores de comparación para simplificar código
    # if 0 < edad < 100 -----------------> esta línea comprueba que la edad sea mayor que 0 y menor que 100

# Operadores lógicos:
    # and === &&
    # or  === ||
    # in ---> comprueba que un valor existe en una lista (list, tuple, dict)

# utilizar lower() y upper() a la hora de checkear strings. Python es case sensitive

def evaluacion():
    nota = int(input("Introduce la nota del alumno: ")) # el input SIEMPRE considera que el valor introducido es un string)

    if nota < 5:
        return "Suspendido"
    elif nota == 10:
        return "Matrícula de honor"
    elif nota == 9:
        return "Excelente"
    elif nota >= 7:
        return "Notable"
    elif nota == 6:
        return "Bien"
    else:
        return "Suficiente"

def concatenarOperadores():
    edad = int(input("Introduce la edad del alumno: "))

    if 0 < edad < 100:
        return "La edad es correcta"
    else:
        return "Edad incorrecta"

def concatenarOperadores2():
    salarioPresidente     = int(input("Introduce salario presidente: "))
    salarioDirector       = int(input("Introduce salario director: "))
    salarioJefe           = int(input("Introduce salario jefe: "))
    salarioAdministrativo = int(input("Introduce salario administrativo: "))

    if salarioAdministrativo < salarioJefe < salarioDirector < salarioPresidente:
        return "OK"
    else:
        return "NOK"

def ifelse_function():
    print(evaluacion())
    print(concatenarOperadores())
    print(concatenarOperadores2())

ifelse_function()