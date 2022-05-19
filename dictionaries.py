#Un diccionario en Python es una colección de elementos, donde cada uno tiene una llave key y un valor value 

product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "firstName": "victor",
    "lastName": "Balladares"
}

print(type(person))#Para saber el tipo de dato

#Metodos de los dictionaries
print(dir(person)) #Nos muestra los métodos de dictionaries

print(person.keys())#Para obtener los valores de las llaves

print(person.items())#Para obtener los items, nos devuelve un tupla

#del person #Borra el dicionario

#Para limpiar el elemento
person.clear()
print(person)

#Una lista puede estar conformada con varios diccionarios
products = [
    {"name": 'book', 'price': 10.99},
    {"name": 'laptop', 'price': 500 }
]
print(products)