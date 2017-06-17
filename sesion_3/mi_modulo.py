# _*_ coding: utf8 _*_

import random

# Creamos una funcion llamada contenido(nombre)
# que recibe el nombre del archivo que vamos a abrir
def contenido(nombre):
    # Abrimos el archivo en modo lectura
    f = open(nombre, "r")
    # Leemos el contenido del archivo
    # y lo guardamos en la variable `texto`
    texto = f.read()
    # Cerramos el archivo
    f.close()
    # Regresamos el contenido del
    # archivo guardado en la variable `texto`
    return texto

# Creamos la funcion llamada colocar(nombre, texto)
# que inserte el contenido de la variable `texto`
# en el archivo con el nombre dado
def colocar(nombre, texto):
    # Abrir el archivo en modo escritura
    f = open(nombre, "w")
    # Colocar el contenido de la variable `texto`
    # en archivo
    f.write(texto)
    # Cerrar el archivo
    f.close()

# Creamos la funcion llamada contenido_falso(nombre, n)
# y genera n numeros aleatorios y los coloca
# dentro del archivo
def contenido_falso(nombre, n):
    # Abrir el archivo
    f = open(nombre, "w")
    # Repetir `n` veces:
    for i in range(n):
        # Genera un numero aleatorio
        x = random.randint(0, 9)
        # Guardalo en archivo
        f.write("%d\n" % x)
    # Cerrar el archivo
    f.close()

# github.com/badillosoft/python-scib