# Importamos el modulo `mi_modulo.py`
# mediante el alias `mm`
import mi_modulo as mm

# Escribimos contenido en el archivo `test.txt`
mm.colocar("test.txt", "Hola mundo\nEste es un mensaje de prueba")
# Escribimos contenido en el archivo `test2.txt`
mm.colocar("test2.txt", "Mas datos de prueba\n:D")

# Recupera e imprime el contenido
# del archivo `test2.txt`
print mm.contenido("test2.txt")
# Recupera e imprime el contenido
# del archivo `test.txt`
print mm.contenido("test.txt")

# Crea 10 numeros aleatorios y los guarda
# en el archivo `numeros.txt`
mm.contenido_falso("numeros.txt", 10)
# Recupera e imprime el contenido
# del archivo `numeros.txt`
print mm.contenido("numeros.txt")