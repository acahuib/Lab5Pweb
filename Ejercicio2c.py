from interpreter import draw
from chessPictures import *
from picture import Picture

# Crear una instancia de Picture para la reina blanca
reina_blanca = queen

# Crear una fila de cuatro reinas blancas
fila_reinas = reina_blanca.join(reina_blanca).join(reina_blanca).join(reina_blanca)

# Dibujar la fila de reinas blancas
draw(fila_reinas)

