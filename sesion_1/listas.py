# _*_ coding: utf8 _*_

###############################################
# Alan Badillo <badillo.soft@hotmail.com>     #
# v1.0 jun 2017                               #
# Es programa recorre una lista de números    #
# indice por indice                           #
###############################################

a = [1, 5, 8, 11, 21, 34, 55, 99]

# len(lista) devuelve el número de elementos
# en lista

# calculamos el nùmero de elementos en la lista
n = len(a)

# Recorremos el rango de 0 a n-1
for i in range(n):
    # Imprimimos el valor de la lista
    # en el indice <i>
    print a[i]