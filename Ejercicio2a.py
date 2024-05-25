from picture import Picture
from interpreter import draw
from pieces import SQUARE, KNIGHT  # Importa las imágenes de las fichas desde pieces.py

# Define las imágenes de las fichas de ajedrez
caballo_negro = Picture(KNIGHT)
caballo_blanco = Picture(KNIGHT)

# Combina las casillas y los caballos en una fila
fila1 = caballo_blanco.join(caballo_negro)

# Repite la fila dos veces para formar un cuadrado
cuadrado = fila1.verticalRepeat(2)

# Dibuja las cuatro casillas con los caballos
draw(cuadrado)

