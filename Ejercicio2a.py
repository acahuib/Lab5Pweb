from interpreter import draw
from chessPictures import *
from picture import Picture

# Crear una instancia de Picture para el caballo blanco
caballo_blanco = knight

# Crear una fila de caballos blancos
fila1 = caballo_blanco.join(caballo_blanco)

# Repetir la fila para formar dos filas de caballos blancos
cuadrado = fila1.verticalRepeat(2)

# Dibujar el cuadrado con los caballos blancos
draw(cuadrado)

