from interpreter import draw
from chessPictures import *
from picture import Picture

# Crear una instancia de Picture para el cuadrado
cuadrado = square

# Crear una fila de ocho cuadrados
fila_cuadrados = cuadrado.horizontalRepeat(8)

# Dibujar la fila de cuadrados
draw(fila_cuadrados)

