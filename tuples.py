#Las tuplas se definen por medio de parentesis
x = (1,2,3)
print(x)
print(type(x))

months = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio')
print(months)

#para saber todos los metodos de una tupla usamos dir
print(dir(x))

print(months[4])#Podemos sacar el valor del indice
#Las tuplas son valores inmutables, no se pueden reasignar
x[4] = 10 #Esto genera un error

#Para eliminar una tupla usamos 
# del x