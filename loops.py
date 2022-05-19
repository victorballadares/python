#El bucle for es una iteración que recorre los elementos de una secuencia ordenada como listas, diccionarios, tuplas, cadenas, etc. 

foods = ['apples','break','cheese','milk']

for food in foods:
    print(food)


colors = ['green','pink','violet','orange','magenta']
for color in colors:
    if color == "pink":
        print("El color es rosa")

for color in colors:
    if color == 'violet':
        break #rompe el código cuando lo encuentra
    print(color)


for color in colors:
    if color == 'violet':
        continue #sigue con el código pero ignora al valor violet
    print(color)

#Utilizando for en range
for number in range(1, 8):
    print(number)

#Iterando caracteres
for letter in "hello":
    print(letter)

#                ****************** Bucle  while *************************

count = 4
while count <= 10:
    print(count)
    count += 1 #Sumamos uno al contador (Si no estuviera crearia un bucle infinito)