# ***Tipos de datos***

#String
# Un string puede ir tipeado de esta manera
print("hello world")
print('hello world')
print('''hello world''')
print("""hello world""")

#Para saber el tipo de dato usamos type seguido del dato a comprobar
print(type("Hello word"))

# Concatenar string
print("bye " + "world")


# *** Numbers
# Integer
print(30)

# Float
print(30.5)

print(type(30))

# Boolean
True
False
print(type(True))

# List
#Podemos cambiar las listas
print([10, 20, 30, 55])
print(["Hello", "Bye", "Adios"])
print([10,"Hello",True, 10.1])
print(type([1,2,"hello"]))
[]

# Tuples
#A diferencia de las listas las tuplas no se pueden cambiar son datos inmutables
print((10,20,30,55))
print(())

# Dictionaries
#Nos permiten agrupar datos que estan definidos por clave y valor.
{"name":"Victor",
"apellido":"Balladares",
"lenguaje":"Python"}

print(type(
{
    "latitud":123422134,
    "long":1234343565434
}))