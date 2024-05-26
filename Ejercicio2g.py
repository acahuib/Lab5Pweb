from interpreter import draw
from chessPictures import *
from picture import Picture

# Crear cuadros claro y oscuro
cuadro_claro = square
cuadro_oscuro = square.negative()

# Crear una fila de cuadros intercalados
fila_cuadros_1 = cuadro_claro.join(cuadro_oscuro).horizontalRepeat(4)
fila_cuadros_2 = cuadro_oscuro.join(cuadro_claro).horizontalRepeat(4)

# Crear el tablero completo intercalando las filas de cuadros
tablero = fila_cuadros_1.under(fila_cuadros_2).verticalRepeat(4)

# Colocar las piezas en sus posiciones iniciales
fila_piezas_negras = rook.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rook)
fila_peones_negros = pawn.horizontalRepeat(8)
fila_peones_blancos = fila_peones_negros.verticalMirror()
fila_piezas_blancas = fila_piezas_negras.verticalMirror()

# Colocar las filas de piezas sobre el tablero
tablero_con_piezas = fila_piezas_negras.under(fila_peones_negros).under(tablero).under(fila_peones_blancos).under(fila_piezas_blancas)

# Dibujar el tablero con las piezas
draw(tablero_con_piezas)

