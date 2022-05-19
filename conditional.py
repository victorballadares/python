#Control de flujo =
#Nos ayudan a controlar esa toma de decisiones utilizando la lógica en nuestros programas.

n1 = 40
if n1 < 20:
    print("n1 es menor que 20")
else:
    print("x es mayor que 20")

color = "blue"
if color == "red":
    print("el color es rojo")
elif color == "blue":
    print("el color es azul")
else:
    print("el color no es rojo")

# ****** Anidar condicionales *****
name = "Victor"
lastName = "Balladares"

if name == "Victor": # Con == comparamos si son iguales

    if lastName == "Balladares":
        print("Tu eres Victor B.....")
    else:
        print("Tu no eres Victor B...")

else:
    print("Tu no eres Victor")


#Operadores lógicos
if x > 2 and x <= 10:
    print("X es mayor que 2 y menor o igual que 10")

if x > 2 or <= 20:
    print("X es mayor que 2 o menor igual a 20")

if (not(x == y)):
    print("x no es igual a y")
