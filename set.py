#Colección desordenada que no tiene indice

colors = {'Red','Green','Blue'}

print(type(colors)) #Para saber el tipo de dato

#Para saber si un dato esta en la colección colors
print('Red' in colors)
colors.add('Violet')
colors.add('Orange')
print(colors)

#Para remover usamos remove
colors.remove('Red')
print(colors)

#Para limpiar el set
#colors.clear()
print(colors)

#para eliminar usamos del seguido del nombre del set a borrar
# del colors 