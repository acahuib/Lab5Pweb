from interpreter import draw
from chessPictures import *
from picture import Picture

# Crear una instancia de Picture para el caballo blanco
caballo_blanco = knight

# Crear una instancia de Picture para el caballo negro invertido
caballo_negro = knight.negative()

# Crear una fila con un caballo blanco y luego un caballo negro
fila1 = caballo_blanco.join(caballo_negro)

# Crear una fila con un caballo negro y luego un caballo blanco
fila2 = caballo_negro.join(caballo_blanco)

# Unir las dos filas para formar una cuadrícula de 2x2 con caballos alternados
cuadricula = fila1.under(fila2)

# Dibujar la cuadrícula final
draw(cuadricula)

