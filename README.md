<br>
<i><b>Autores:</b></i> Natalia Salas y Catalina Perdomo - 6º semestre
<br>
<i><b>Asignatura:</b></i> Parallel and Distributed Computing
<br>
<b>Ciencias de la computación e inteligencia artificial</b></i>

# Comparativa-de-rendimiento-Cython-vs-Python

Python al ser un lenguaje de programación interpretado, es lento a comparación del lenguaje de programación C que es compilado. Para resolver este problema se puede traducir el código Python a C y compilándolo con Cython y así obtener de esta forma considerables mejoras del rendimiento. Cython es un lenguaje de programación que fusiona Python con el sistema de tipos estáticos de C y C ++. Este traduce el código fuente de Cython a un código fuente de C eficiente y se puede compilar en un módulo de extensión de python o en un ejecutable independiente.

El objetivo principal de la siguiente practica de laboratorio es hacer una comparativa cython/python para evaluar el rendimiento de estos lenguajes con la implementación de tres algoritmos diferentes. Se elaboro una batería de experimentos para controlar el ruido gaussiano y posteriormente evaluar el tiempo de ejecución al utilizar el mismo algoritmo en cython y python. Para cada ejercicio a su vez se realizó una comparativa con la primera versión de cython y una versión de cython mejorada.

A continuación, se encontrarán tres carpetas, cada una contiene un algoritmo:
- **DistanceLevenshtein:** Mide el número mínimo de ediciones de un solo carácter necesarias para cambiar una palabra por la otra. En esta carpeta se encuentran los diferentes ficheros en los que se encuentran la implementación y solución del problema:
> - *levenshtein_cy.pyx:* En este archivo se encuentra la resolución del algoritmo en lenguaje de programación Cython 
> - *levenshtein_py.py:* En este archivo se encuentra la resolución del algoritmo en lenguaje de programación Python 
> - *principal.py:* Este programa realiza la ejecución de Cython y Python, para poder realizar esto, este programa escrito en ```.py``` implementará ambos programas como bibliotecas y de esta modalidad accede a sus respectivos procedimientos con la resolución. Por ultimo imprime el tiempo de ejecución del ```.pyx``` y ```.py```.
> - *setup.py:* Este fichero es el crea el objeto compartido y genera la extensión de Cython al compilarlo.
> - *Makefile:* Este archivo define un conjunto de tareas a ejecutar, contiene las órdenes que debe ejecutar la utilidad make

- **Montecarlo:** Estima en valor de PI con la siguiente formula: $π=4*\frac{SUPERFICIE\ CIRRCULO}{SUPERFICIE\ CUADRADO}$ .  En esta carpeta se encuentran los diferentes ficheros en los que se encuentran la implementación y solución del problema:
> - *montecarlo_cy.pyx:* En este archivo se encuentra la resolución del algoritmo en lenguaje de programación Cython 
> - *levenshtein_py.py:* En este archivo se encuentra la resolución del algoritmo en lenguaje de programación Python 
> - *montecarlo_py.py:* Este programa realiza la ejecución de Cython y Python, para poder realizar esto, este programa escrito en ```.py``` implementará ambos programas como bibliotecas y de esta modalidad accede a sus respectivos procedimientos con la resolución. Por ultimo imprime el tiempo de ejecución del ```.pyx``` y ```.py```.
> - *setup.py:* Este fichero es el crea el objeto compartido y genera la extensión de Cython al compilarlo.
> - *Makefile:* Este archivo define un conjunto de tareas a ejecutar, contiene las órdenes que debe ejecutar la utilidad make..

- **OrdenamientoQuickSort:** Consiste en ordenar los elementos de un arreglo de tal forma que todos los menores queden a la izquierda y todos los mayores a la derecha. En esta carpeta se encuentran los diferentes ficheros en los que se encuentran la implementación y solución del problema:
> - *quickSort_cy.pyx:* En este archivo se encuentra la resolución del algoritmo en lenguaje de programación Cython 
> - *quickSort_py.py:* En este archivo se encuentra la resolución del algoritmo en lenguaje de programación Python 
> - *principal.py:* Este programa realiza la ejecución de Cython y Python, para poder realizar esto, este programa escrito en ```.py``` implementará ambos programas como bibliotecas y de esta modalidad accede a sus respectivos procedimientos con la resolución. Por ultimo imprime el tiempo de ejecución del ```.pyx``` y ```.py```.
> - *setup.py:* Este fichero es el crea el objeto compartido y genera la extensión de Cython al compilarlo.
> - *Makefile:* Este archivo define un conjunto de tareas a ejecutar, contiene las órdenes que debe ejecutar la utilidad make

##Ejecución:
En primera instancia, estos ficheros se deben ejecutar en un entorno Linux. Para poder ejecutar los algoritmos por separado, se deben seguir los siguientes pasos: 
1. En una terminal ejecute el comando ```make all```, con este se creara el objeto compartido y compila los archivos ```.py``` y ```.pyx```..
2. Luego ejecute el comando ```python3 principal.py```, con este obtendrá los tiempos de ejecución de los lenguajes guardados en un archivo ```.csv```.


