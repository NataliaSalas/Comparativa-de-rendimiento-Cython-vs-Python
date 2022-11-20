import montecarlo_py
import montecarlo_cy
import time
    
#Declaración de variables
n=1000000

#Se crea formato para la impresion sobre el fichero
formato_datos = "{:.5f},{:.5f},{:.5f}\n"
#Definición de experimentos 
#Reducción ruido Gaussiano
for i in range(30):
    #Toma de tiempos para Py
    ini_time = time.time()
    montecarlo_py.montecarlo(n)
    fin_time = time.time()
    time_python = fin_time-ini_time

    #Toma de tiempos para Cy
    ini_time = time.time()
    montecarlo_cy.montecarlo(n)
    fin_time = time.time()
    time_cython = fin_time-ini_time

    with open("montecarlo.csv","a") as archivo:
        archivo.write(formato_datos.format(time_python, time_cython,time_python/time_cython))
    print("Cython Time: ",time_cython)
    print("Python Time: ",time_python)

    print("Cython es: ",time_python/time_cython," mas rapido")