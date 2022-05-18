myStr = "hello,world"
print("My name is "+myStr) #Concatenación tipica
print(f"My name is {myStr}") #Indicamos mediante llaves lo que se debe concatenar
print("My name is {0}".format(myStr)) #Concatenamos con format
#print(dir(myStr))

#Metodos
print(myStr.upper()) #Convierte todo a mayusculas
print(myStr.lower()) #Convierte todo a minusculas
print(myStr.swapcase()) #Convierte las minusculas en mayusculas y viceversa
print(myStr.capitalize()) #Convierte la primera en mayucula el resto lo mantiene igual
print(myStr.count('l')) #Cuenta la veces que aparece el caracter l
print(myStr.count('o'))
print(myStr.startswith('hola')) #Para saber si la cadena empieza por hola. (true or false)
print(myStr.startswith('hello'))
print(myStr.startswith('he'))
print(myStr.endswith('world')) #Para saber si la cadena termina con esa frase
print(myStr.endswith('d'))
#print(myStr.split()) #Separa mi cadena apartir de los espcios en blanco , o caracteres que pases 
print(myStr.split(','))
# print(myStr.split('o'))
print(myStr.find('o')) #Busca el caracter y nos da su indice
print(len(myStr)) #Nos imprime la longitud de la cadena
print(myStr.index('e')) #Nos imprime donde comienza el caracter buscado en que posición ese encuentra
print(myStr.isnumeric()) #Preguntamos que si la variable es numerica
print(myStr.isalpha())  #Preguntamos que si la variable es alfanumerica
print(myStr[0]) #Imprime el caracter de la posición que le indico
print(myStr[1]) #Imprime el caracter de la posición que le indico
print(myStr[2]) #Imprime el caracter de la posición que le indico
print(myStr[3]) #Imprime el caracter de la posición que le indico
print(myStr[4]) #Imprime el caracter de la posición que le indico
print(myStr[-1]) #Nos imprime el último caracter de la cadena 
print(myStr[-2]) #Nos imprime el último caracter de la cadena 
print(myStr[-3]) #Nos imprime el último caracter de la cadena 
print(myStr[-4]) #Nos imprime el último caracter de la cadena 
print(myStr[-5]) #Nos imprime el último caracter de la cadena 

#Métodos encadenados
print(myStr.replace('hello', 'bye').upper()) #Reemplaza el texto que indicamos y lo pasa a mayusculas gracias el método upper