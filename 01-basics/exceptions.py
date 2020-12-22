# Sintaxis de las EXCEPTIONS:

try:
    # code
except Exception:
    # code
finally:
    # code

# la instrucción RAISE permite modificar exceptions propias del lenguaje
# además de crear exceptions propias
raise ZeroDivisionError("Mensaje customizado para la exception")