# _*_ coding: utf-8 _*_

# Una empresa requiere saber en que
# categoría están sus clientes
# respecto a las siguientes categorías

# A - de 0 a 11 años
# B - de 12 a 16 años
# C - de 17 a 24 años
# D - 24 a 31 años
# E - Otros

# Crear un programa que solcite
# la edad y responda con la categoría
# en la que se encuentra la persona

edad = int(raw_input("Dame la edad: "))

if edad >= 0 and edad <= 11:
    print "A"
elif edad >= 12 and edad <= 16:
    print "B"
elif edad > 16 and edad < 25:
    print "C"
elif edad >= 25 and edad < 32:
    print "D"
else:
    print "E"

# int
# float
# str
# bool
# None
print type(edad) == int