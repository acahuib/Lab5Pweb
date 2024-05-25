from interpreter import draw
from chessPictures import *
from picture import Picture

# Crear una instancia de Picture para el cuadrado blanco y su inverso (negro)
cuadrado_blanco = square
cuadrado_negro = square.negative()

# Crear una fila de 8 cuadrados alternando entre el cuadrado inverso y el normal
fila_cuadrados = cuadrado_negro.join(cuadrado_blanco).horizontalRepeat(4)

# Crear la cuadrícula de 8x4 con cuadrados alternando en el patrón del tablero de ajedrez
cuadricula = fila_cuadrados.verticalRepeat(4)

# Dibujar la cuadrícula de cuadrados
draw(cuadricula)

