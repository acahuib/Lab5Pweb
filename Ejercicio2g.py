from interpreter import draw
from chessPictures import *
from picture import Picture

# Crear una fila de 8 fichas blancas alternando entre bishop, king, knight, pawn, queen, rock y square
fila_blanca = bishop.join(king).join(knight).join(pawn).join(queen).join(rock).join(square).horizontalRepeat(8)

# Crear una fila de 8 fichas negras alternando entre bishop, king, knight, pawn, queen, rock y square
fila_negra = bishop.negative().join(king.negative()).join(knight.negative()).join(pawn.negative()).join(queen.negative()).join(rock.negative()).join(square.negative()).horizontalRepeat(8)

# Crear la cuadrícula de ajedrez de 8x8 con fichas alternando en el patrón estándar
cuadricula_ajedrez = fila_blanca.under(fila_negra).verticalRepeat(4)

# Dibujar la cuadrícula de ajedrez
draw(cuadricula_ajedrez)

