#Manejo de paquetes

#pip = para instalar librerias externas a python
import numpy #pip install numpy

print(numpy.version.version)

numpy_array =numpy.array([35,24,62,52,30,30,17])
print(type(numpy_array))

print(numpy_array * 2)

#import pandas #pip install pandas
#pip install pip --- Instalar pip
#pip --version saber que version de pip tenemos
#pip list listado de paquetes instalados
#pip uninstall "nombre de paquete" desinstalar un paquete
# pip show "nombre de paquete" ver informacion de un paquete

import requests #pip install requests
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json()) #traendo los primeros 151 pokemons

#Paquete arithmetics
from my_package import aritmetics

print(aritmetics.sum_two_values(1,4))


