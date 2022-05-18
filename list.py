# ** List **

demo_list = [1,"hello", 1.34, True, [1,2,3]]
print(len(demo_list))
colors = ['green','blue','orange']
colors[1] = 'magenta' #cambiamos el color que tenemos por el nuevo que asignamos mediante indice
print(colors)
print(type(colors))
print(dir(colors)) #Metodos posibles a usar
print(len(colors)) #Para saber la longitud de la lista
print(colors[2])
print('green' in colors) #Nos muestra con un booleano si se encuentra el color en la lista
print('violet' in colors)
#colors.append(('pink','yellow')) #Agregamos un nuevo valor a la lista, pero para pasar dos argumentos tenemos que pasarlo a tupla
#Pero para pasarlo como una lista tenemos que usar un metodo llamado extend
colors.extend(('pink','yellow')) #Asi logramos tener elementos dentro de una lista
print(colors)
#Como insertamos un valor antes de otro
colors.insert(1,'Black') #Colocando el indice y el color agregar
#Insertar al final el color
colors.insert(len(colors), 'red')
print(colors)
#Para quitar el ultimo color de la lista, sile ejecutas más veces lo borra
colors.pop()
print(colors)
#Para remover un valor exacto usamos remove
colors.remove('green')
print(colors)
colors.pop(3)#Indicamos que elimine el indice 3
print(colors)
#Para ordenar una lista usamos el metodo sort
colors.sort()
print(colors)
#Ahora para ordenar a la inversa usamos reverse
colors.sort(reverse=True)
print(colors)
#Como saber el indice de la lista
print(colors.index('orange'))
#para contar cuantas veces aparece en la lista
print(colors.count('red'))

numbers_list = list((1,2,3,4)) 

rango_de_lista = list(range(1,11)) #Range genera una lista desde el numero indice que le pongas hasta el final que le indiques
print(rango_de_lista)

