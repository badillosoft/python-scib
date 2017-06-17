import matplotlib.pyplot as plt
import numpy as np

# Generar un arreglo con 10 numeros
# igualmente distribuidos entre [-PI, PI]
x = np.linspace(-np.pi, np.pi, 10)

# Aplicar la funcion sin() a cada elemento de x
# devuelve un arreglo de la misma longitud que x
y = np.sin(x)

# Graficar los puntos de `x` y `y`
plt.plot(x, y, "r-") # r-- r+ r* b- bo

# Mostrar la grafica
plt.show()