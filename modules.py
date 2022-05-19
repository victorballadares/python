# Un módulo o module en Python es un fichero .py que alberga un conjunto de funciones, variables o clases y que puede ser usado por otros módulos.

#Modulo propio
#Bibliotecas que podemos descargar de internet
#Modulo de las bibliotecas de python

#Tenemos que importar los modulos para usarlos
import datetime
# o tambien podemos usarlo como sale a a continuación
# from datatime import timedelta => nos redirije a dentro del metodo datatime y asi poder usar solo timedelta(minutes=70) sin usar datetime

print(datetime.date.today()) #Nos indica la fecha actual
print(datetime.timedelta(minutes=70)) #Transforma minutos a hora

#Importanto modulo propio creado en el archivo myMath.py
from myMath import add, substract

#reutilizamos codigo
add(5,2)
substract(10,4)

#Importando modulo descargado de internet
from colorama import Fore, Style, init
init(convert=True)
print(Fore.RED + "Que color es") #Cambiamos la salida del color de código