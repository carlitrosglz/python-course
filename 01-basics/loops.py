# BUCLE FOR
    # for VARIABLE in ARRAY

array = ["raton", "gato", "elefante", "perro"]

for i, item in enumerate(array):
    print(f"[{i}]: {item}")

# recorrer strings con un for
for char in "correo@correoelectronico.com":
    print(char, end = "") # el parametro END permite modificar el final de la impresion de un print()

########################################################################3

email = "pepe@email.com"
valido = False

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("Email correcto")
else:
    print("No valido")

# BUCLE WHILE