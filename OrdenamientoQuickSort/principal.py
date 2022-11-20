"""
La idea principal es crear un ".csv" con la toma de timpos 
"""
import quickSort_py
import quickSort_cy
import time
from random import sample
    
#Declaración de variables
#a = [78, 67, 34, 35, 89, 56]
a = sample(range(1,601),600)

#Se crea formato para la impresion sobre el fichero
formato_datos = "{:.5f},{:.5f},{:.5f}\n"
#Definición de experimentos 
#Reducción ruido Gaussiano
for i in range(30):
    #Toma de tiempos para Py
    ini_time = time.time()
    quickSort_py.ordenar(a)
    fin_time = time.time()
    time_python = fin_time-ini_time

    #Toma de tiempos para Cy
    ini_time = time.time()
    quickSort_cy.ordenar(a)
    fin_time = time.time()
    time_cython = fin_time-ini_time

    with open("quickSort.csv","a") as archivo:
        archivo.write(formato_datos.format(time_python, time_cython,time_python/time_cython))
    print("Cython Time: ",time_cython)
    print("Python Time: ",time_python)

    print("Cython es: ",time_python/time_cython," mas rapido")