from picture import Picture
from interpreter import draw
from pieces import SQUARE, KNIGHT  # Importa las imágenes de las fichas desde pieces.py

# Define las imágenes de las fichas de ajedrez
caballo_negro = Picture(KNIGHT)
caballo_blanco = Picture(KNIGHT)

# Combina las casillas y los caballos en una fila
fila1 = caballo_negro.join(caballo_blanco)
fila2 = fila1.verticalRepeat(2)  # Repite la fila dos veces para formar un cuadrado

# Dibuja las cuatro casillas con los caballos
draw(fila2)
