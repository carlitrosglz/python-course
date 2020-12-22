def generaNumerosPares(limit):
    num = 1

    while num < limit:
        # YIELD construye un Iterable que contiene (en este caso) la lista con los numeros pares correspondientes
        # Entrega los valores de uno en uno, por lo que será necesario ir llamando al método .next() del Iterable
        # para obtener toda la lista
        yield num * 2
        num += 1

lista = generaNumerosPares(10)

# for item in lista:
#     print(item)

print(next(lista))
print(next(lista))
print(next(lista))

##########################################################

def devuelveCiudades(*ciudades): # el asterisco indica al compilador que no se sabe la cantidad exacta de argumentos a enviar. Se enviará una tupla
    for item in ciudades:
        #for subItem in item:
            #yield subItem
            yield from item

ciudadesGenerator = devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudadesGenerator))
print(next(ciudadesGenerator))




