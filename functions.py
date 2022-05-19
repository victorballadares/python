# Una función es una porción o bloque de código reutilizable que se encarga de realizar una determinada tarea.

#Funciones que hemos visto ya
# print()
# dir(x)
# type(12)

#Función propia => se definen con la palabra def
def hello(name="Person"): #colocando ="Person le decimos que pase por defecto ese valor"
    print("Hello",name) #concatenamos el nombre

hello("Victor") # Llamamos a la función para que se ejecute
hello("Diego") # Llamamos a la función para que se ejecute
hello("Lola") # Llamamos a la función para que se ejecute
hello("Esmeralda") # Llamamos a la función para que se ejecute
hello()

#Funcion con numeros
def add(n1, n2):
    return n1 + n2

print(add(10,30))
print(add(650,80))
print(len("hello"))#Nos dice la cantidad de caracteres

#Funcion lambda

add = lambda n1, n2: n1 + n2 #Reemplazamos la palabra def por lambda
print(add(25,7))