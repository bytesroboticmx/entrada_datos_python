#Programa que utiliza entrada de datos del usuario con funciones de python estandar.
#Autor: Aldo Gonzalez Vazquez
#Licencia: MIT

entrada = input("Introduce un mensaje: ")
print("El mensaje introducido es: ", entrada)

#Funcion que convierte a minusculas
print("El mensaje introducido en minusculas es: ", entrada.lower())

#Funcion que convierte a mayusculas
print("El mensaje introducido en mayusculas es: ", entrada.upper())

#Funcion que convierte la primera letra en mayuscula
print("El mensaje introducido con la primera letra en mayusculas es: ", entrada.capitalize())

#Funcion que invierte una cadena coompleta
print("El mensaje introducido invertido es: ", entrada[::-1])

#Funcion que reemplaza una cadena por otra.
print("El mensaje introducido reemplazado es: ", entrada.replace("a", "e"))

#Funcion que corta una cadena en una posicion determinada
print("El mensaje introducido cortado es: ", entrada[0:2])

#Funcion que utliza split para separar una cadena en una lista.
print("El mensaje introducido separado es: ", entrada.split(" "))

#Funcion que utiliza strip para eliminar espacios en blanco.
print("El mensaje introducido sin espacios es: ", entrada.strip())

#Funcion que utiliza join para unir una lista.
print("El mensaje introducido unido es: ", " ".join(entrada))

#Funcion que utliza starwith para saber si una cadena empieza con una letra.
print("El mensaje introducido empieza con la letra a: ", entrada.startswith("a"))

#Funcion que utiliza endswith para saber si una cadena termina con una letra.
print("El mensaje introducido termina con la letra a: ", entrada.endswith("a"))

#Funcion que utiliza find para saber si una cadena contiene una letra.
print("El mensaje introducido contiene la letra a: ", entrada.find("a"))

#Funcion que utiliza count para saber cuantas veces se repite una letra en una cadena.
print("El mensaje introducido contiene la letra a: ", entrada.count("a"))

#Funcion que utiliza isalnum para saber si una cadena contiene caracteres alfanumericos.
print("El mensaje introducido contiene caracteres alfanumericos: ", entrada.isalnum())

#Funcion que donde aparece una letra con un cierto tiempo de aparicion.
print("El mensaje introducido contiene la letra a: ", entrada.index("a"))


